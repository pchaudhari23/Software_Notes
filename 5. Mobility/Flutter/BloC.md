FEATURES:

- State management library.
- In built widgets in flutter_bloc
- Seperate the presentation layer from business logic. Connects the Usecase and UI.
- event -> bloc -> state
- UI -> i. dispatch events to the bloc, ii. react to the states from the bloc.
- FLOW: UI -> Bloc -> Call to Usecase -> Repository(Impl) -> DataSource
- Business logic in clean architecture is to call usecase
  4 files:
  1.feature_bloc
  2.feature_event: started, inprogress, done etc
  3.feature_state: empty, loading, loaded, error etc
  4.barrel file: all file export

Every widget has a bloc, which maintains state?

---

EVENT:

- Event is an interaction of the user with the application on the UI. Eg: Pressing a button, Entering text in the textfield etc.
- Based on the input given by the user, some action needs to be taken like making an API call or showing something on the UI etc.
- In Summit project, usually two events are frequently used : for assetList, incidentList and serviceList

1. GetListData - To display the data in the list form on the UI.
2. LoadMoreData - To display more data in the list on scrolling down.

- The GetData event has declarations of the API request parameters as they will be required to make the API Request call.
- LoadMore contains instance of entity and state.
- Since events are fired from the UI, the API request parameters which are declared in the event class get the values from the widget.
- In widget, we declare the request parameters and assign them value which are then passed to the event by calling 'add' method on the BlocProvider.

---

STATE:

- State is the value of variables defined in the stateful flutter widgets.
- Usually 4 types of states are frequently used in Summit project:

1. Initial - Contains just the class declaration,
2. Loading - Usually contains progress indicator
3. Loaded - Conatains the instance of entity class to display properties of the entity object in the UI on load
4. LoadFailure - to display error in case of API call failure or LoginLogout failure.

- State is changed on the UI and on state change (change of variables defined in stateful widget), the widget is re-rendered.

---

BLOC:

- Bloc has declarations for Usecase class and it is initialised in the Bloc's constructor.
- It has two methods:

1. initialState - Calls the initial state from state class
2. mapEventToState -

- this method takes the main event class as argument and returns a stream of states class.
- uses a sequence of if else conditions to call a particular state on occurance of a particular event.
- the if else condition block in turn call methods defined after the mapEventToState method. The event class parameters are passed as arguments to these methods.
- one of these methods (which may return a Future or Stream of state class) calls the 'call' method from the usecase thus connecting the bloc to the usecase.
- the call method returns an either called 'result' on which the fold method is applied.
- before the call to the usecase is made, the usecase params class object is created and assign or initialise the values of parameters and then pass that to the call method.

---

PAGES:

- Uses the widgets created in the widgets folder.
- Contains code for appbar, item list widget in the Scaffold widget, bloc initialisation, dependency etc.

---

WIDGETS:

- Create small, individual, reusable widgets which will be called in the page.
- Mainly two widgets are used:

1. Item widget - UI code for the card which display individual item (for assets, incidents, service request).
2. Item list widget - Conatains UI code for the list of Item widget cards, it is built using the listview builder which takes two arguments - itemcount is the length of the entity object list and itembuilder is the resable item widget part.

- Widgets have two declarations -
  i. an instance of entity class whose data is to be displayed on UI or parameters to be used for some operation,
  ii. instance of bloc - to be consumed somewhere from which the event will be fired.
- Use widget.entityobject.property to display it or use it in widget code.

---

MISCELLENEOUS:

1. async\* - the asterik means that this is an async generator which is used to insert data in the stream of states. A stream is a sequence of asynchronous data. It is similar to async keyword which is used while returning a Future.
2. yeild - keyword which is used to output the states in the stream of states in the bloc.
3. fold - it is a method which is applied on an Either.
   an Either returns Failure or Entity/Model object as success which is later handeled in the fold method.
   fold has two parameters - (failure) - handels failure retured by either,
   (entity object) - handels the entity object returned by either on success.

---

BLOC WIDGETS:

- Bloc is written in the bloc file of the bloc folder but in order to consume it in the UI we use inherited bloc widgets which come in the flutter_bloc package. The types of bloc widgets are

1. BlocBuilder
2. BlocProvider
3. MultiBlocProvider
4. BlocListener
5. MultiBlocListener
6. BlocConsumer
7. RepositoryProvider
8. MultiRepositoryProvider

- Out of which, BloC widgets 1 to 5 are frequently used in the Summit project.

---

BlocBuilder:

- Returns or re-renders a widget whenever the state of that widget changes.
- Takes a builder argument.
- SYNTAX:
  BlocBuilder<BlocA, StateA>(
  bloc: //optional
  builder: (context, state) {
  if (state is ....){
  return 'render a widget / call a function which renders a widget'
  }
  else if (state is ....){
  return 'render a widget / call a function which renders a widget'
  }
  else if (state is ....){
  return 'render a widget / call a function which renders a widget'
  }
  },
  )

---

BlocProvider & MultiBlocProvider

- Provides the BloC instance to it's child widget where it can be used in the a BlocBuilder or a BlocListener
- MultiBlocProvider is used when many BloC instances need to be passed to the child widget. Uses a provider array with list of BloCs to improve readability.
- SYNTAX:
  BlocProvider(
  create: (\_) => dependency<BlocA>(),
  child: Widget,
  ),

---

BlocListener & MultiBlocListener

- Used to listen to the state changes and take an action on change like displaying a widget or re-rendering an existing widget.
- Returns a void and re-renders the widget only once per state change.
- Takes a listner argument
- SYNTAX:
  BlocListener<BlocA, StateA>(
  listner: (context, state) {
  if (state is ....){
  'render a widget / call a function which renders a widget'
  }
  else if (state is ....){
  'render a widget / call a function which renders a widget'
  }
  else if (state is ....){
  'render a widget / call a function which renders a widget'
  }
  },
  child : BlocBuilder<BlocA, StateA>() OR a widget
  )

---
