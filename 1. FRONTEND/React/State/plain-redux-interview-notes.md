# Plain Redux — Interview Notes

Scope: classic Redux (`createStore`, `connect`, HOC pattern) — the pre-hooks, pre-RTK way of doing things. Interviewers ask about this to test whether you understand *why* Redux Toolkit exists, and whether you can read legacy codebases.

---

## 1. What problem does Redux solve?

- React's own state is local to a component tree — sharing state across distant components means prop-drilling or lifting state up, which gets unmanageable as the tree grows.
- Redux gives you a **single global store** that any component can read from or dispatch actions to, without passing props through every intermediate layer.
- It also makes state changes **predictable and traceable** — every change happens through a dispatched action and a pure reducer, which is what enables features like time-travel debugging (Redux DevTools) and easier testing.

## 2. Three core principles

1. **Single source of truth** — the entire app state lives in one store (one JS object tree).
2. **State is read-only** — the only way to change state is to dispatch an action (a plain object describing what happened). Components never mutate state directly.
3. **Changes are made with pure functions** — reducers take `(previousState, action)` and return a new state. Same inputs must always produce the same output, no side effects, no mutation.

## 3. Actions

An action is a plain JS object with a mandatory `type` field (usually a string constant) and optional payload:

```js
export const FETCH_USERS = 'FETCH_USERS';
export const FETCH_USERS_SUCCESS = 'FETCH_USERS_SUCCESS';

export const fetchUsers = () => ({ type: FETCH_USERS });
export const fetchUsersSuccess = (users) => ({
  type: FETCH_USERS_SUCCESS,
  payload: users,
});
```

- `fetchUsers` here is an **action creator** — a function that returns an action object. You dispatch the *result* (`dispatch(fetchUsers())`), not the function itself.
- Interview trap: "what's the difference between an action and an action creator?" — an action is the plain object; an action creator is the function that builds it.

## 4. Reducers

```js
const initialState = { list: [] };

export default function usersReducer(state = initialState, action) {
  switch (action.type) {
    case FETCH_USERS_SUCCESS:
      return { ...state, list: action.payload };
    default:
      return state;
  }
}
```

**Reducer rules (frequently asked):**
- Must be pure — no API calls, no random values, no `Date.now()`, no mutating arguments.
- Must return a new state object on change (never mutate `state` directly — always spread/copy).
- Must return the *existing* state unchanged for unknown action types (the `default` case).
- Must handle an `undefined` state by falling back to `initialState` (this is how the store bootstraps on first run — Redux dispatches an internal init action against every reducer).

### combineReducers

```js
import { combineReducers } from 'redux';
export default combineReducers({ users, posts, comments });
```

- Combines multiple slice reducers into one root reducer. Each key becomes a top-level branch of the state tree (`state.users`, `state.posts`, etc.).
- Each sub-reducer only ever sees and returns its own slice of state — it has no access to sibling slices.

## 5. Store

```js
import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga';
import rootReducer from './reducers';
import rootSaga from '../sagas/rootSaga';

const sagaMiddleware = createSagaMiddleware();
export const store = createStore(rootReducer, applyMiddleware(sagaMiddleware));
sagaMiddleware.run(rootSaga);
```

- `createStore(reducer, [preloadedState], [enhancer])` — creates the store.
- `applyMiddleware(...)` is a **store enhancer** — it wraps `dispatch` so every dispatched action passes through the middleware chain before reaching the reducer.
- Store exposes: `getState()`, `dispatch(action)`, `subscribe(listener)`.

## 6. Middleware — what it actually is

- A function that sits between `dispatch` and the reducer, in the shape: `store => next => action => { ... }`.
- Lets you intercept actions to do things reducers can't (since reducers must be pure/synchronous): logging, async calls, side effects.
- Without middleware, Redux can only handle synchronous, plain-object actions. This is *why* you need something like Saga or Thunk for API calls — dispatching a promise or a function directly isn't valid unless middleware supports it.
- **Thunk** middleware lets you dispatch a function instead of an object; Redux calls that function with `(dispatch, getState)`.
- **Saga** middleware lets you dispatch plain actions as normal, but a "watcher" generator function listens for specific action types and runs side-effect logic (`call`, `put`, etc.) in response — decoupled from the dispatch call itself.

## 7. connect() — the pre-hooks binding layer

```js
import { connect } from 'react-redux';
import { compose } from 'redux';

const UsersContainer = ({ users, fetchUsers, fetchPosts }) => {
  useEffect(() => { fetchUsers(); }, [fetchUsers]);
  return <UsersList users={users} onUserClick={fetchPosts} />;
};

const mapStateToProps = (state) => ({
  users: state.users.list,
});

const mapDispatchToProps = {
  fetchUsers,
  fetchPosts,
};

export default connect(mapStateToProps, mapDispatchToProps)(UsersContainer);
```

- `connect` is a **higher-order component (HOC)** — it takes your component and returns a new wrapped component that's subscribed to the store.
- It re-renders the wrapped component whenever the *selected* slice of state changes (shallow-compared), not on every store update — this is actually one of `connect`'s real strengths: built-in render optimization without you writing `useMemo`.

### mapStateToProps

- A function: `(state, ownProps?) => object`.
- Whatever it returns gets merged into the component's props.
- `state` here is the *entire* Redux store — you pick out only what this component needs.
- Second optional arg `ownProps` lets you compute derived props based on props passed from the parent (e.g., filtering by an `id` prop).

### mapDispatchToProps

- Two forms:
  1. **Object shorthand** (shown above) — react-redux automatically wraps each action creator in `dispatch(...)` for you.
  2. **Function form**: `(dispatch) => ({ fetchUsers: () => dispatch(fetchUsers()) })` — gives explicit control, useful when you need to dispatch conditionally or combine multiple actions in one prop function.
- If you omit `mapDispatchToProps` entirely, `connect` injects `dispatch` itself as a prop — you'd manually call `dispatch(fetchUsers())` in the component.

### compose

```js
export default compose(connect(mapStateToProps, mapDispatchToProps))(UsersContainer);
```

- `compose` is a utility to chain multiple HOCs left-to-right execution (right-to-left application) without deep nesting: `compose(a, b, c)(x)` === `a(b(c(x)))`.
- With only one HOC (just `connect`), `compose` is functionally unnecessary — it's there for when you're layering multiple HOCs (e.g., `connect` + `withRouter` + `withStyles`).

### Why containers/components split?

- "Container" (or "smart") components: connected to Redux, know about `dispatch`/state, contain logic.
- "Presentational" (or "dumb") components: pure UI, receive everything via props, no store awareness.
- This was the standard architecture pre-hooks. It's less strictly followed today since hooks let any component talk to the store directly, but interviewers may still ask you to explain the pattern and its intent (separation of concerns, reusability, easier testing of presentational components in isolation).

## 8. connect() vs hooks (useSelector / useDispatch)

| | `connect` (HOC) | Hooks |
|---|---|---|
| Pattern | Wraps component, injects props | Called directly inside function component |
| Boilerplate | `mapStateToProps`/`mapDispatchToProps` functions | Direct `useSelector(fn)` / `dispatch(action)` calls |
| Re-render optimization | Automatic shallow-compare on selected state | You control it — each `useSelector` call is independently compared by reference |
| Class components | Required (only way to connect a class component) | Not usable — hooks only work in function components |
| Current status | Legacy — still works, still exists in older codebases | Standard/idiomatic since react-redux v7+ |

**Common interview question: "Why did the community move from connect to hooks?"**
- Less boilerplate — no need to write/maintain two mapping functions per component.
- No wrapper component in the React tree (easier debugging in DevTools).
- Easier to colocate multiple slices of state without stacking `compose`.
- Function components + hooks became the default React style overall, so `connect`'s HOC pattern felt increasingly out of step.

## 9. Redux vs Context API (frequent question)

- Context solves *prop drilling*, not state management — it has no built-in concept of actions, reducers, middleware, or devtools.
- Context re-renders **every consumer** of a context when its value changes, unless you manually memoize/split contexts — Redux's `connect`/`useSelector` only re-render components whose *selected* slice actually changed.
- Redux gives you middleware for async/side-effect orchestration (thunk, saga); Context gives you nothing built-in — you'd hand-roll it with `useEffect` inside a provider.
- Rule of thumb to state in an interview: Context is fine for slow-changing, narrowly-scoped state (theme, auth flag, current locale). Redux is better once you have complex, frequently-updated, cross-cutting state or need middleware-driven async orchestration.

## 10. Common mistakes / gotchas (frequently probed)

- **Mutating state directly in a reducer** — e.g., `state.list.push(item)` instead of returning a new array. Breaks reference-equality checks that `connect`/`useSelector` rely on for re-renders.
- **Side effects in reducers** — API calls, random values, timestamps inside a reducer. Reducers must be pure; side effects belong in middleware (thunk/saga) or the action-dispatching component.
- **Forgetting the default case** in a `switch` reducer — must return existing state for unrecognized actions, or you'll return `undefined` and break the store.
- **Not providing a default parameter for state** — `function reducer(state = initialState, action)` — omitting `= initialState` breaks store bootstrapping.
- **Overusing global state** — putting every piece of UI state (e.g., "is this dropdown open") into Redux instead of local `useState`. Not everything needs to be global.
- **Deeply nested state shapes** — makes updates verbose (deep spreading) and reducers error-prone. Prefer normalized state (flat, keyed by ID) for anything relational — a commonly asked design question.

## 11. Normalizing state (likely to come up)

Instead of:
```js
{ posts: [{ id: 1, comments: [{ id: 10, text: '...' }] }] }
```

Prefer:
```js
{
  posts: { byId: { 1: { id: 1, commentIds: [10] } }, allIds: [1] },
  comments: { byId: { 10: { id: 10, text: '...' } }, allIds: [10] },
}
```

- Avoids deeply nested updates (updating one comment doesn't require rewriting the whole posts array).
- Avoids duplicate data if the same entity appears in multiple lists.
- This is the exact problem `@reduxjs/toolkit`'s `createEntityAdapter` solves out of the box — worth mentioning if asked "how would RTK help here."

## 12. Quick-fire Q&A

**Q: What's the difference between `state` and `props` in a connected component?**
A: `props` come from the parent component (or route); `state` (via `mapStateToProps`) comes from the Redux store. `connect` merges both into what the wrapped component receives.

**Q: Can you dispatch multiple actions from one function?**
A: Not as a single plain action — but with thunk middleware, a thunk function can call `dispatch` multiple times; with sagas, a saga can `put` multiple actions in sequence.

**Q: What does `applyMiddleware` actually return?**
A: A store enhancer — a function that modifies how the store is created, specifically wrapping `dispatch` so actions pass through the middleware chain first.

**Q: Why use action type constants instead of inline strings?**
A: Avoids typos causing silent bugs (a reducer/saga listening for `'FETCH_USER'` while the action dispatches `'FETCH_USRE'` fails silently — no error, just nothing happens). Constants centralize the type in one place, importable everywhere.

**Q: What is `getState()` used for, and when would you call it in middleware?**
A: Returns the current state tree. Used inside thunks/saga `select()` calls when you need to read existing state before deciding what to dispatch next (e.g., avoid re-fetching data you already have).

**Q: Is Redux still relevant given React's built-in state tools (useReducer + Context)?**
A: Yes, for apps with complex cross-cutting state, need for middleware-driven async orchestration, or dev-tooling requirements (time-travel debugging, action logging). For smaller apps, `useReducer` + Context often suffices — this is itself a common interview discussion point, not a settled "always use X" answer.

---

## Summary table: connect API surface

| API | Purpose |
|---|---|
| `connect(mapStateToProps, mapDispatchToProps)(Component)` | Wraps component, injects state + dispatch-bound actions as props |
| `mapStateToProps(state, ownProps?)` | Selects which store data becomes props |
| `mapDispatchToProps` (object or function) | Defines which action creators become callable props |
| `Provider` | Makes the store available to the component tree via context, required at the root |
| `compose(...)` | Chains multiple HOCs together |
