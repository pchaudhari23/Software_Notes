REDUX: State management library

1. redux: compose(), combineReducers()
2. react-redux: useSelector(), useDispatch()
3. redux-saga: call() - worker saga, put() - worker saga, takeEvery() - watcher saga, takeLatest() - watcher saga, all() - root saga, createSagaMiddleware() - configureStore
4. immer: produce()
5. reselect (already included in toolkit by default): createSelector(), createStructuredSelector()
6. redux-persist: persistReducer(), createMigrate()
7. redux-injectors: createInjectorsEnhancer()
8. @reduxjs/toolkit: createSlice(), createAction(), combineReducers(), createReducer(), configureStore(), getDefaultMiddleware()
9. @types/react-redux: React with typescript

- redux-logger
- redux-devtools-extension
- eslint-plugin-redux-saga

---

```
prop-types:
Component.defaultProps = {}
Component.propTypes = {}
```

---

1]

```
import PropTypes from 'prop-types';
....
....
....
componentName.proptypes = {
key:value,
}
```

key - Prop name
value - Proptypes. (datatype/ oneOfType)

---

2]

```
componentName.defaultProps = {
key:value,
}
```

key - Prop name
value - default value for that prop

---

3]

```
import { createStructuredSelector } from 'reselect';
....
....
....
const mapStateToProps = createStructuredSelector({
key:value,
})
```

OR

```
const mapStateToProps = (state) => {
return {
key: value <----- state object
}
}
```

key - variable which contains the data received from the store. Used to display info in the UI
value - selector function imported from selectors file

NOTE: Whatever key is mentioned in mapStateToProps must be passed as props to the component
Component can take props argument which can be destructured later, or individual props

---

4]

```
const mapDispatchToProps = (dispatch) => {
return {
dispatch,
key:value,
};
}
```

OR

```
const mapDispatchToProps = dispatch => ({
dispatch,
key:value,
});
```

key - action which is passed to dispatch method. this action comes in component through prop
value - action imported from actions file
dispatch is a method - takes action - dispatch()
Eg: dispatch(action_imported_from_actions_file({payload object}))

NOTE: Whatever key is mentioned in mapDispatchToProps must be passed as props to the component
Component can take props argument which can be destructured later, or individual props

---

5]

```
import { connect } from 'react-redux';
.....
.....
.....
const withConnect = connect(
mapStateToProps,
mapDispatchToProps
);
```

---

6]

```
import { compose } from 'redux';
.....
.....
.....
export default compose(withConnect)(componentName);
```

---

STATE:

- Passing state around components in DOM tree is hard.
- So state of all components, the entire application state is placed in a global object called store.
- Dispatch action from UI -> Call API -> Save the fetched data in store -> Retrive the data from store

1. A component re-renders when there is change in props or state.
2. You can only change the state. You cannot change the prop of a component. Props are read only
3. Use minimum possible state variables in any component as they can cause unnecessary re-rendering. Instead useRef can be used to save any value
4. State variables are stored in memory. If many state variables are used unnecessarily, the application will take up lot of memory and become heavy or slow.
5. So even if memory is cheapest piece of hardware technology, developer should be a miser when allocating it in code.

---

ACTIONS:

- Javascript object: Type (string store in constants file) and payload properties.
- 3 Action types: Main action | Failure | Success
- Initial State: Loading | Error | Status
- Status: Idle | Process | Failure | Success | Data
- 2 files: 1.Actions - File containing all constants of action types, 2.Action Creators - File containing action functions
- Actions are dispatched from component. From within useEffect with payload if the data is required when component renders.
- Dispatch method takes action object.

---

REDUCERS:

- Function with two arguments: 1.Initial state (defined in the same file), 2.Action object
- Contains switch case with action.type as argument. Perform operations based on action type.
- Returns an object (the updated state) based on previous input.
- State should not be mutated. Create a shallow copy of action.paload object using spread opearator.
- Reducers must be pure functions.
- current state + action -> reducer (normal JS function) -> updated state

---

MIDDLEWARE:

- Used to perform async operations like API requests and handle side effects.
- API request can return data at any time depending on network. So yeild is used which keeps listening and returns a stream of data handeled using generator function.
- Middleware occurs between action and reducer. Because API calls happen when an action is dispatched (from a component eg: button, link click) and reducer has to update the state in response to the dispatched action.
- Side effect manager. Eg:Redux Saga, Redux Thunk, Observables(RxJS)

GENERATOR FUNCTION:

- Allows us to pause the function execution and resume instead of executing all the statements of function in one pass.
- Returns an iterable -> iterator is something which allows us to iterate over multiple values returned by the generator function
- Use yield keyword to obtain the values
- Uses \* after function keyword
- Use next() method on object returned by generator function
- next() method returns an object -> {value: ..... , done: ......}
- value is the value returned by the yield, done is a boolean which indicates completion status, becomes true when the generator encounters a return statement.

---

REDUX SAGA:

- An ES6 generator function which is a seperate thread in the application solely responsible to manage the side effects, handle async actions.

Types of saga:

1. rootSaga - contains the array of all watcher sagas
2. watcherSaga - watches or listens to the actions dispatched from the UI and calls worker saga accordingly
3. workerSaga - does work!!! make calls to the backend to get the data (using yeild call) and set the received data in store state (using yeild put).

In worker saga:

- call - asynchronous action eg: API Call
- put - dispatch action to redux store, set data in the store
- select

In watcher saga:

- takeEvery: Call saga on every event like clicking a button
- takeLatest: Call saga on last or latest event

API function -> watcher saga -> actions -> Worker saga -> root saga

---

REDUX TOOLKIT:

1. createSlice():

- Create slices of reducer as per the feature or functionality or requirement eg: reducer slice for authentication, reducer slice for data display from api call etc.
- Object with 3 properties: 1.Name of slice, 2.Initial state, 3. Reducer object with key and value pairs unlike reducer in traditional redux which is a function and switch case

  2. combineReducer():

- combine all the reducers slices. Object with the keys as slice name.
- Object with reducer and middleware properties

  3.Types - types of payloads - type is an interface you export

  4.Slice - A file that contains actions and reducers for a particular feature of the application

  5.Selector:

- To get the data stored in the store object - store.getState()
- To update the state - store.dispatch()
- Actions are dispatched to the reducers which are like event listners.
- Selectors - getters of data from redux store
- Reducers - setters of data in redux store

---

MISC:

- useDispatch(): to dispatch an action. Gives dispatch function which takes action object.
- useSelector(): to obtain the data from redux store
- connect(): used to connect react to redux. connected components are sometimes called containers.
- mapStateToProps(): Expose the state of store in props of component. Calls the selectors using useSelector.
- mapDispatchToProps()
- mapStateToProps & mapDispatchToProps are called on every state change, on re-renders.
- When mapStateToProps is called the selectors are called again and latest data from the store is saved in the selector variables. The selector variables are present in props.

---
