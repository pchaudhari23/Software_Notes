# Redux-Saga — Interview Deep-Dive Notes

Scope: everything saga-specific — generator fundamentals, effects, watcher/worker pattern, common flows, testing, and saga-vs-thunk tradeoffs. Given your background, expect the deepest interview questions to land here.

---

## 1. Why does Saga exist? (expect this as an opener)

- Reducers must be pure and synchronous — they can't make API calls, can't dispatch other actions, can't have side effects.
- Something has to sit outside the reducer to handle async work (API calls, timers, websockets) and then dispatch plain actions back into the store once that work resolves. That's what **middleware** is for.
- Saga's specific angle versus other middleware (thunk): side-effect logic is written as **generator functions**, which lets you pause execution, express complex async control flow (parallel calls, racing, cancellation, retries) in a way that reads like synchronous code, and — critically — makes that logic **testable without mocking**, since a generator yields plain descriptions of effects rather than actually performing them.

## 2. Generator fundamentals (you may get asked this directly)

```js
function* worker() {
  console.log('start');
  const result = yield 'pause point';
  console.log('resumed with', result);
}
```

- A generator function (`function*`) doesn't run its body immediately when called — calling it returns an **iterator** object.
- `.next()` resumes execution until the next `yield`, and returns `{ value, done }`.
- `yield` pauses the function and hands control back to whoever is driving the iterator (here, that's the saga middleware).
- **Key insight interviewers want you to say:** when a saga does `yield call(api)`, it isn't calling the API itself — it's *yielding a plain object* describing "call this function with these args." The saga middleware receives that object, actually performs the call, and feeds the result back into the generator via `.next(result)`. This is why sagas are unit-testable: you can assert on the yielded effect object without ever hitting a real network call.

## 3. Effects — the core vocabulary

| Effect | Purpose |
|---|---|
| `call(fn, ...args)` | Calls a function (often returning a Promise) and waits for the result. Yields a *description* of the call — testable without executing it. |
| `put(action)` | Dispatches an action to the Redux store. |
| `take(actionType)` | Pauses the saga until a matching action is dispatched — manual, one-off listening. |
| `takeEvery(actionType, worker)` | Spawns a new worker for **every** matching action, concurrently. No cancellation of previous instances. |
| `takeLatest(actionType, worker)` | Spawns a worker for each matching action, but **automatically cancels the previous instance** if it's still running when a new one comes in. |
| `takeLeading(actionType, worker)` | Runs the first matching action's worker, **ignores** further matches until that worker finishes. |
| `fork(fn, ...args)` | Starts a non-blocking child task — the saga continues without waiting for it. Errors in a forked task propagate to the parent (crashes it) unless caught. |
| `spawn(fn, ...args)` | Like `fork`, but the child task is **detached** — its errors don't crash the parent saga. |
| `all([...])` | Runs multiple effects in parallel, waits for all to complete — like `Promise.all`. |
| `race({ a: effectA, b: effectB })` | Runs effects in parallel, resolves as soon as **one** completes, cancels the rest — like `Promise.race`. |
| `select(selectorFn)` | Reads a value from the current Redux state, inside the saga. |
| `delay(ms)` | Pauses execution for a given time (from `redux-saga/effects` or `redux-saga`'s utils) — commonly used for debounce/polling. |
| `cancel(task)` | Cancels a running task (from `fork`/`takeLatest` etc). |
| `cancelled()` | Inside a saga, checks whether the current task was cancelled — used to clean up in a `finally` block. |
| `debounce(ms, actionType, worker)` | Built-in helper — waits for a quiet period after the last matching action before running the worker. Equivalent to manually combining `delay` + `takeLatest`. |
| `throttle(ms, actionType, worker)` | Runs the worker on the first matching action, then ignores further matches for `ms`, regardless of how many come in. |
| `retry(count, delayMs, fn, ...args)` | Retries a function up to `count` times with a delay between attempts, throws if all attempts fail. |

## 4. Watcher / worker pattern (expect this by name)

```js
function* fetchUsersWorker() {
  const users = yield call(api.fetchUsers);
  yield put(fetchUsersSuccess(users));
}

function* usersSaga() {
  yield takeLatest(FETCH_USERS, fetchUsersWorker); // watcher
}
```

- **Watcher**: listens for a specific action type, decides when/how to invoke the worker (`takeEvery`/`takeLatest`/`takeLeading`/`debounce`/`throttle`).
- **Worker**: does the actual side-effect work (the API call, dispatching success/failure).
- Splitting them this way is the standard convention — it makes the concurrency strategy (every/latest/leading/debounced) swappable without touching the actual side-effect logic.

## 5. takeEvery vs takeLatest vs takeLeading — the most commonly asked comparison

| | Concurrent instances | Use case |
|---|---|---|
| `takeEvery` | Runs all, no cancellation | Independent actions where order/overlap doesn't matter (e.g., logging every click) |
| `takeLatest` | Cancels previous when new one starts | Search-as-you-type, any "only the newest request matters" scenario |
| `takeLeading` | Ignores new triggers until current finishes | Prevent double-submit (e.g., "Place Order" button spam-clicked) |

**Trap question:** "Does `takeLatest` cancel the in-flight HTTP request, or just ignore its result?" — Answer: it cancels the **saga task**, which means if the worker was doing `yield call(fetchApi)`, the underlying promise still resolves in the background (fetch/axios calls aren't truly abortable by saga alone unless you wire up an `AbortController` and handle it in a `finally`/`cancelled()` block) — but the saga stops processing the result and won't dispatch further actions from that cancelled task. Worth mentioning `AbortController` if asked to *actually* cancel the network request, not just ignore its result.

## 6. Debounced search — a canonical example

```js
function* searchWorker(action) {
  yield delay(400); // wait for typing to pause
  try {
    const results = yield call(api.search, action.payload);
    yield put(searchSuccess(results));
  } catch (e) {
    yield put(searchFailure(e.message));
  }
}

function* watchSearch() {
  yield takeLatest(SEARCH, searchWorker);
}
```

- `takeLatest` + a leading `delay` inside the worker is the manual way to debounce.
- The built-in `debounce(400, SEARCH, searchWorker)` effect does the same thing more concisely — mention both; knowing the manual version proves you understand *why* debounce works (cancel-on-new-action + wait), not just that the helper exists.

## 7. Parallel fetch — `all`

```js
function* loadPostDetail(action) {
  const postId = action.payload;
  const [comments, author] = yield all([
    call(api.fetchComments, postId),
    call(api.fetchAuthor, postId),
  ]);
  yield put(loadDetailSuccess({ comments, author }));
}
```

- Both calls fire concurrently, saga waits for both. If either throws, the whole `all` rejects (like `Promise.all`) — worth wrapping in `try/catch` to dispatch a single failure action.

## 8. Race + cancellation — timeout pattern

```js
function* fetchWithTimeout(action) {
  const { response, timeout } = yield race({
    response: call(api.fetchData, action.payload),
    timeout: delay(5000),
  });

  if (timeout) {
    yield put(fetchFailure('Request timed out'));
  } else {
    yield put(fetchSuccess(response));
  }
}
```

- `race` is the standard pattern for "give up after N seconds" — whichever effect resolves first wins, the other is auto-cancelled.
- Same shape works for "cancel this fetch if the user navigates away":

```js
yield race({
  detail: call(fetchDetailWorker, postId),
  cancel: take(SELECT_POST), // fires if user clicks a different post
});
```

## 9. Retry with backoff

```js
function* fetchWithRetry(action) {
  try {
    const data = yield retry(3, 1000, api.fetchData, action.payload);
    yield put(fetchSuccess(data));
  } catch (e) {
    yield put(fetchFailure(e.message));
  }
}
```

- `retry(maxTries, delayMs, fn, ...args)` is a built-in effect — retries up to `maxTries`, throws the last error if all attempts fail.
- If asked to implement *exponential* backoff (not fixed delay), you write it manually:

```js
function* fetchWithBackoff(action, maxAttempts = 3) {
  let attempt = 0;
  while (attempt < maxAttempts) {
    try {
      const data = yield call(api.fetchData, action.payload);
      yield put(fetchSuccess(data));
      return;
    } catch (e) {
      attempt++;
      if (attempt >= maxAttempts) {
        yield put(fetchFailure(e.message));
        return;
      }
      yield delay(2 ** attempt * 500); // exponential: 1s, 2s, 4s...
    }
  }
}
```

## 10. Polling (long-running saga loop)

```js
function* pollComments(postId) {
  try {
    while (true) {
      const comments = yield call(api.fetchComments, postId);
      yield put(commentsUpdated(comments));
      yield delay(20000);
    }
  } finally {
    if (yield cancelled()) {
      // cleanup if needed
    }
  }
}

function* watchPostDetail() {
  while (true) {
    const { payload: postId } = yield take(OPEN_POST);
    const task = yield fork(pollComments, postId);
    yield take(CLOSE_POST);
    yield cancel(task);
  }
}
```

- `fork` starts the polling loop without blocking; storing the returned task lets you `cancel()` it later (e.g., when the user navigates away).
- `finally` + `cancelled()` is the standard cleanup pattern — checking whether the task ended due to cancellation vs completing normally, useful for resource cleanup (clearing timers, closing sockets).

## 11. Optimistic updates + rollback

```js
function* likePostWorker(action) {
  const { postId } = action.payload;
  yield put(likeOptimistic(postId)); // update UI immediately

  try {
    yield call(api.likePost, postId);
  } catch (e) {
    yield put(likeRollback(postId)); // revert on failure
    yield put(showError('Failed to like post'));
  }
}
```

- Dispatch the "assume success" state change first for instant UI feedback, then reconcile with a rollback action if the actual call fails.
- Interview framing: this is a UX pattern enabled by *any* async middleware, but sagas make the rollback branch explicit and easy to read linearly (`try` succeeds → done; `catch` → rollback), versus chaining `.then().catch()` in a thunk.

## 12. select() — reading state inside a saga

```js
function* fetchMyPostsWorker() {
  const userId = yield select((state) => state.currentUser.id);
  const posts = yield call(api.fetchUserPosts, userId);
  yield put(fetchMyPostsSuccess(posts));
}
```

- Lets a saga read the store without needing the triggering action to carry that data in its payload.
- Common use: reading auth/current-user state, checking "do I already have this cached" before re-fetching, reading a filter/pagination value set elsewhere.

## 13. Error handling patterns

- **Always wrap `call` effects in `try/catch`** inside the worker — an uncaught error in a saga can crash that saga task (and depending on `fork` vs `spawn`, potentially the parent).
- Standard shape: dispatch a `*_FAILURE` action in the `catch` block with the error message, which a `uiSlice`/error reducer picks up for a banner/toast.
- `fork` vs `spawn` matters here: an error in a `fork`ed child **propagates up** and can crash the parent saga; a `spawn`ed child's error is isolated — the parent keeps running. Use `spawn` for "fire and forget" tasks you don't want bringing down the rest of the saga tree if they fail.

## 14. Testing sagas (mention even without writing tests — shows awareness)

```js
import { call, put } from 'redux-saga/effects';

it('fetches users', () => {
  const gen = fetchUsersWorker();
  expect(gen.next().value).toEqual(call(api.fetchUsers));
  expect(gen.next(mockUsers).value).toEqual(put(fetchUsersSuccess(mockUsers)));
  expect(gen.next().done).toBe(true);
});
```

- Because `call`/`put` yield plain **effect descriptions** rather than executing anything, you can step through a saga generator manually with `.next()` and assert on each yielded value — no mocking `fetch`/axios required.
- `redux-saga-test-plan` is a common library that makes this less verbose (`expectSaga(...).put(...).dispatch(...).run()`), worth naming if asked how you'd test a large saga.

## 15. Saga vs Thunk — the classic comparison question

| | Thunk | Saga |
|---|---|---|
| Style | Function returning a function `(dispatch, getState) => {...}`, uses `async/await` | Generator function, uses `yield` with declarative effects |
| Complex async (race, retry, cancel) | Manual — hand-roll with `Promise.race`, `AbortController`, custom retry loops | Built-in effects (`race`, `retry`, `cancel`, `takeLatest`) |
| Testability | Harder — usually requires mocking `fetch`/`dispatch` | Easier — effects are plain objects, step through with `.next()` |
| Boilerplate for simple fetch-on-click | Less | More (watcher + worker + effects) |
| Learning curve | Low — just async/await | Higher — generators, effect vocabulary |
| Long-running processes (websockets, polling with pause/resume) | Awkward | Natural fit (`fork`/`cancel`/`while(true)` loops) |
| Industry trend (2026) | Default via `createAsyncThunk` in RTK | Still used, especially in older/larger codebases with complex async flows |

**Strong answer if asked "when would you choose Saga over Thunk today":** for genuinely complex async orchestration — race conditions, cancellable long-running processes (polling, websocket subscriptions), retry/backoff logic, or when you need to react to actions independently of where they were dispatched from (decoupling trigger from effect). For simple CRUD fetch-on-mount/fetch-on-click, thunk (or RTK Query) is less code for the same result — don't claim sagas are "just better," claim they solve a specific class of problem that thunks handle awkwardly.

## 16. Common mistakes / gotchas

- **Forgetting `try/catch` around `call`** — an unhandled rejection inside a saga either crashes the task or silently fails depending on fork type; always handle it explicitly.
- **Using `takeEvery` where `takeLatest` was needed** — e.g., search-as-you-type with `takeEvery` fires a worker per keystroke with no cancellation, so slow/out-of-order responses can overwrite newer ones ("race condition" in the literal sense — an older, slower response arrives after a newer one and clobbers it).
- **Not cancelling polling loops on unmount/navigate-away** — a `while(true)` + `delay` loop started with `fork` keeps running forever unless explicitly `cancel()`ed, leaking background requests.
- **Confusing `fork` and `call`** — `call` blocks the saga until the called function/generator finishes; `fork` starts it and continues immediately. Using `call` where you wanted concurrent/non-blocking behavior is a common bug.
- **React 18 StrictMode double-invoking effects in dev** — if a saga is triggered from a component's `useEffect` without a cleanup/guard, StrictMode's intentional double-invoke in development can fire the saga twice, which is often mistaken for a saga bug rather than a React dev-mode behavior. Worth knowing to correctly diagnose it live if asked or if it comes up.

## 17. Quick-fire Q&A

**Q: What does `yield` actually pause — the saga or the middleware?**
A: The generator function itself pauses at each `yield`. The saga middleware drives the generator forward by calling `.next()`, performing whatever effect was yielded, and feeding the result back in.

**Q: Why can't you just `await` inside a saga instead of using effects?**
A: You technically can mix `async/await` with generators in some setups, but doing so loses the point of sagas — effects being plain, inspectable objects is what makes `call`/`put` testable without mocking and cancellable by the middleware. Using raw `await` for a call bypasses the middleware's ability to intercept and cancel it.

**Q: What happens if two `takeLatest` workers for the same action are somehow both in flight?**
A: They can't be — that's the entire point of `takeLatest`: starting a new instance automatically cancels any still-running previous instance of that specific watched action's worker.

**Q: Difference between `take` and `takeEvery`?**
A: `take` is a one-shot listen — the saga pauses once, resumes when the action fires, then continues past that point (used for manual loops like the polling example). `takeEvery` is a helper that internally loops and forks a new worker on every matching action, indefinitely.

**Q: How would you handle two dependent sequential API calls where the second needs data from the first?**
A: Plain sequential `yield call(...)` — no special effect needed. `all([...])` is only for calls that can run *concurrently*; if call B needs call A's result, they're inherently sequential and you just `yield` them one after another in order.

---

## Summary table: effect cheat sheet

| Need | Effect |
|---|---|
| Call an async function | `call(fn, ...args)` |
| Dispatch an action | `put(action)` |
| React to every matching action | `takeEvery` |
| React to only the latest, cancel stale | `takeLatest` |
| Ignore new triggers until current finishes | `takeLeading` |
| Debounce | `debounce(ms, type, worker)` or manual `delay` + `takeLatest` |
| Throttle | `throttle(ms, type, worker)` |
| Run several calls concurrently | `all([...])` |
| First-to-finish wins, cancel the rest | `race({...})` |
| Read store state | `select(fn)` |
| Non-blocking background task | `fork` (errors propagate) / `spawn` (errors isolated) |
| Cancel a running task | `cancel(task)` |
| Retry on failure | `retry(count, delayMs, fn, ...args)` or manual loop for backoff |
| Pause execution | `delay(ms)` |
