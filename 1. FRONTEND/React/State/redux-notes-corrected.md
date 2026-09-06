# REDUX: State management library — Corrected Notes

> Corrected version of the original notes. Fixes applied: `mapStateToProps` vs `useSelector` conflation, `combineReducers` vs `configureStore` mixup, saga runtime flow diagram, and the `yield` "listening" description. Everything else from the original is preserved as-is since it was accurate.

---

## Package/API reference

1. **redux**: `compose()`, `combineReducers()`
2. **react-redux**: `useSelector()`, `useDispatch()`
3. **redux-saga**: `call()` – worker saga, `put()` – worker saga, `takeEvery()` – watcher saga, `takeLatest()` – watcher saga, `all()` – root saga, `createSagaMiddleware()` – used when configuring the store
4. **immer**: `produce()`
5. **reselect** (already included in toolkit by default): `createSelector()`, `createStructuredSelector()`
6. **redux-persist**: `persistReducer()`, `createMigrate()`
7. **redux-injectors**: `createInjectorsEnhancer()`
8. **@reduxjs/toolkit**: `createSlice()`, `createAction()`, `combineReducers()`, `createReducer()`, `configureStore()`, `getDefaultMiddleware()`
9. **@types/react-redux**: React with TypeScript

- redux-logger
- redux-devtools-extension
- eslint-plugin-redux-saga

---

## prop-types

```
Component.defaultProps = {}
Component.propTypes = {}
```

### 1. PropTypes

```js
import PropTypes from 'prop-types';
// ...
componentName.propTypes = {
  key: value,
};
```

- `key` — prop name
- `value` — PropType (datatype / `oneOfType`)

### 2. defaultProps

```js
componentName.defaultProps = {
  key: value,
};
```

- `key` — prop name
- `value` — default value for that prop

> Note (not in original): `defaultProps` on function components is deprecated as of React 18/19 — prefer JS default parameters (`const Component = ({ key = value }) => ...}`) in new code. Keep this note if you're documenting legacy patterns for interview recall, but don't write new code this way.

---

## 3. mapStateToProps

```js
import { createStructuredSelector } from 'reselect';
// ...
const mapStateToProps = createStructuredSelector({
  key: value,
});
```

OR

```js
const mapStateToProps = (state) => {
  return {
    key: value, // <----- derived from the state object
  };
};
```

- `key` — variable which contains the data received from the store, used to display info in the UI
- `value` — selector function imported from the selectors file (or an inline expression reading `state`)

**Note (corrected):** `mapStateToProps` is a plain function that reads directly from the Redux `state` object — it does **not** call or use `useSelector` internally. `useSelector` is a separate, hooks-based way of reading from the store, and belongs to function components that don't use `connect()` at all. `connect()`/`mapStateToProps` and `useSelector`/`useDispatch` are two alternative APIs for the same underlying job (reading from the store) — one is HOC-based, the other is hook-based. They aren't layered on top of each other.

NOTE: Whatever key is mentioned in `mapStateToProps` must be passed as a prop to the component. The component can take a `props` argument which can be destructured later, or receive individual props.

---

## 4. mapDispatchToProps

```js
const mapDispatchToProps = (dispatch) => {
  return {
    dispatch,
    key: value,
  };
};
```

OR

```js
const mapDispatchToProps = (dispatch) => ({
  dispatch,
  key: value,
});
```

- `key` — the prop name the component will call to dispatch an action
- `value` — a function that calls `dispatch(actionImportedFromActionsFile({ payload }))`
- `dispatch` is a store method that takes an action object: `dispatch(action)`

NOTE: Whatever key is mentioned in `mapDispatchToProps` must be passed as a prop to the component. The component can take a `props` argument which can be destructured later, or receive individual props.

---

## 5. connect()

```js
import { connect } from 'react-redux';
// ...
const withConnect = connect(mapStateToProps, mapDispatchToProps);
```

---

## 6. compose()

```js
import { compose } from 'redux';
// ...
export default compose(withConnect)(componentName);
```

---

## STATE

- Passing state around components in the DOM tree is hard.
- So the state of all components — the entire application state — is placed in a global object called the store.
- Flow: Dispatch action from UI → Call API → Save the fetched data in the store → Retrieve the data from the store.

1. A component re-renders when there is a change in props or state.
2. You can only change state. You cannot change the props of a component — props are read-only.
3. Use the minimum possible state variables in any component, as they can cause unnecessary re-rendering. `useRef` can be used instead to save any value that doesn't need to trigger a re-render.
4. State variables are stored in memory. If many state variables are used unnecessarily, the application will take up a lot of memory and become heavy or slow.
5. So even though memory is one of the cheapest hardware resources, a developer should still be a miser when allocating it in code.

---

## ACTIONS

- A plain JavaScript object with `type` (a string, usually stored in a constants file) and `payload` properties.
- 3 common action "types" per flow: Main action | Failure | Success.
- Initial state fields typically tracked: Loading | Error | Status.
- Status values: Idle | Process | Failure | Success | Data.
- 2 files convention: 1. **Actions** — file containing all constants of action types. 2. **Action Creators** — file containing action-creating functions.
- Actions are dispatched from a component — often from within `useEffect`, with a payload if the data is required when the component renders.
- The `dispatch` method takes an action object.

---

## REDUCERS

- A function with two arguments: 1. Initial state (defined in the same file, as the default value of the first argument), 2. Action object.
- Contains a `switch` on `action.type`. Performs operations based on the action type.
- Returns an object (the updated state) based on the previous state and the action.
- State should not be mutated. Create a shallow copy using the spread operator (of the previous state and/or `action.payload`, as needed).
- Reducers must be pure functions.
- `current state + action => reducer (a normal JS function) => updated state`

---

## MIDDLEWARE

- Used to perform async operations like API requests, and to handle side effects generally.
- API requests can return data at unpredictable times depending on the network. Saga specifically handles this using generator functions and the `yield` keyword to express "pause here until this resolves" logic in a readable, sequential-looking way.
- Middleware sits between the dispatched action and the reducer — because side effects (like API calls) need to happen in response to a dispatched action, but the reducer itself must stay synchronous and pure, so it can't do that work.
- Middleware is essentially a **side-effect manager**. Examples: Redux Saga, Redux Thunk, Observables (RxJS).

**Corrected note:** `yield` itself does not create a "listening" or "streaming" mechanism — it's a generic generator-function keyword that just pauses execution at that point until something calls `.next()` again. The actual "listening for dispatched actions" behavior comes specifically from saga's watcher effects (`take`, `takeEvery`, `takeLatest`, etc.), which re-invoke a saga each time a matching action is dispatched. `yield` is the pause/resume mechanism generators use generally; the listening behavior is layered on top of it by saga's own effects, not something `yield` does by itself.

---

## GENERATOR FUNCTION

- Allows you to pause function execution and resume it, instead of executing all statements in one pass.
- Calling a generator function returns an **iterator** — something that lets you step through the multiple values the function yields, one at a time.
- Uses the `yield` keyword to produce values.
- Declared with a `*` after the `function` keyword: `function* myGen() { ... }`.
- Call `.next()` on the object returned by the generator function to advance it.
- `.next()` returns an object: `{ value: ..., done: ... }`.
  - `value` is whatever was yielded.
  - `done` is a boolean indicating completion status — becomes `true` once the generator runs to completion or hits a `return`.

---

## REDUX SAGA

- An ES6 generator function that acts as a separate "thread" in the application, solely responsible for managing side effects and handling async actions.

### Types of saga

1. **rootSaga** — contains the array of all watcher sagas, run once via `sagaMiddleware.run(rootSaga)`. It's a registration point, not a step actions flow "through" at runtime.
2. **watcherSaga** — watches/listens for specific actions dispatched from the UI, and invokes the corresponding worker saga when a match occurs.
3. **workerSaga** — does the actual work: makes calls to the backend (`yield call(...)`) and writes the received data into the store (`yield put(...)`).

### In a worker saga

- `call` — perform an asynchronous action, e.g. an API call
- `put` — dispatch an action to the Redux store, setting data in the store
- `select` — read a value from the current store state

### In a watcher saga

- `takeEvery` — runs the worker saga on every matching dispatched action (e.g. every button click), concurrently, no cancellation of earlier runs
- `takeLatest` — runs the worker saga on the latest matching action, automatically cancelling any still-in-flight previous run

**Corrected runtime flow (the original diagram had this backwards):**

> Action dispatched (from UI) → watcher saga (listening for that action type) → worker saga (`call` the API, `put` the result) → reducer updates the store

`rootSaga` is not part of this per-request flow — it's only where all watcher sagas get registered together (via `all([...])`) so `sagaMiddleware.run()` has one combined entry point at app startup.

---

## REDUX TOOLKIT

### 1. createSlice()

- Creates a slice of the reducer per feature/functionality/requirement, e.g. a slice for authentication, a slice for API-fetched data display, etc.
- Takes an object with 3 properties: 1. `name` of the slice, 2. `initialState`, 3. a `reducers` object with key–value pairs (each value is a reducer function for that action) — unlike a traditional Redux reducer, which is a single function with a `switch` statement.

### 2. combineReducers()

- Combines multiple slice reducers into a single root reducer. Takes an object whose keys are the slice names and whose values are each slice's reducer function.
- Returns one root reducer function — no middleware is involved at this step.

**Corrected note:** the "object with `reducer` and `middleware` properties" described in the original notes is actually the config object passed to **`configureStore()`**, not `combineReducers()`. `configureStore({ reducer, middleware })` is where you supply the (already-combined, or per-slice) reducers plus any middleware array; `combineReducers()` itself only ever deals with merging reducer functions.

### 3. Types

- Types of payloads — a `type` is an interface you export (TypeScript context).

### 4. Slice

- A file that contains the actions and reducer logic for a particular feature of the application.

### 5. Selector

- To get data stored in the store object: `store.getState()`.
- To update the state: `store.dispatch()`.
- Actions are dispatched to reducers, which act like event listeners.
- **Selectors** — getters of data from the Redux store.
- **Reducers** — setters of data in the Redux store.

---

## MISC

- **`useDispatch()`** — returns the `dispatch` function, used to dispatch an action object.
- **`useSelector()`** — used to read data from the Redux store, inside a function component.
- **`connect()`** — used to connect a React component to Redux; connected components are sometimes called "containers."
- **`mapStateToProps()`** — exposes store state as props on the component. (Corrected: this reads directly from the `state` argument passed to it by `connect()` — it does not call `useSelector`, which is an entirely separate, hooks-based API.)
- **`mapDispatchToProps()`** — exposes dispatchable action functions as props on the component.
- `mapStateToProps` and `mapDispatchToProps` are re-invoked on every store update the connected component subscribes to (via `connect`'s internal subscription), which is what drives re-renders when the selected state changes.
- Each time `mapStateToProps` runs, its selector logic re-reads the latest data from the store, and the result is passed into the component as props.

---

## Gaps worth adding (not in the original notes)

- `takeLeading` — runs on the first matching action, ignores further triggers until that worker finishes (useful for preventing double-submit).
- `race({...})` — runs multiple effects in parallel, resolves on whichever finishes first, cancels the rest (timeout patterns).
- `fork` / `spawn` — non-blocking child tasks; errors in a `fork`ed task propagate to the parent, `spawn`ed task errors are isolated.
- `retry(count, delayMs, fn, ...args)` — built-in retry-on-failure effect.
- `debounce` / `throttle` — built-in helpers combining `delay` + `takeLatest`/rate-limiting, so you don't have to hand-roll them.
