Links:

https://github.com/ResoCoder/flutter-tdd-clean-architecture-course

https://www.youtube.com/watch?v=KjE2IDphA_U&list=PLB6lc7nQ1n4iYGE_khpXRdJkJEp9WOech

https://resocoder.com/flutter-clean-architecture-tdd/

https://resocoder.com/category/tutorials/flutter/tdd-clean-architecture/

---

FEATURES:

- Seperation of concerns.
- Build scalable, maintainable, testable code.
- Independent of frameworks and libraries.
- loose coupling
- call flow - down, data flow - up
- SOLID, YAGNI, DRY

---

DEPENDENCY INVERSION:

- Repository contains the business logic.
- Repository - Belongs to both data and domain layer.
- Domain layer - Abstract class, data layer - its implementation

---

FOLDER STRUCTURE:

- lib => 2 folders => core, features
- CORE: Contains reusable code, enums, routes, utils, miscelleneous files and functions
- FEATURES => feature wise folders (login, registartion, checkout, payments etc.)
- feature folder:

1. PRESENTATION - bloc, pages, widgets
2. DOMAIN - usecases, entities, repositories
3. DATA - datasources, models, repositories
4. Feature dependency file

---

IMPLEMENTATION:

- Build the dummy UI first.
- start from domain layer => data => presentation
- all the files will have classes, and classes will have methods
- the classes will have objects of the previous class as member variable, and also in constructor

---

DATA FLOW (Model and Entity objects) in CLEAN ARCHITECTURE:
UI (events fired to bloc and states returned from bloc) => Bloc => Usecase => Repository => DataSource => Request Parameters class (to json) => API Request method in Datasource.

- Bloc contains declaration of usecase instance and calls method of usecase.
- Usecase contains declaration of repository instance and calls method of repository.
- Repository implementation contains declaration of datasource instance and calls method of datasource.
- Datasource contains request and parameter object from the request file and calls API request method.

---

DOMAIN LAYER:
1.Usecases:

- usecase should have a call method
- class implements other class
- Take input from BloC
- business logic gets executed here
- UseCase <Entity object which repository method returns, Params class or NoParams>
- repo - function takes request parameters as argument and returns Entity object in Either, wrapped in a Future.
- repo impl - function takes request parameters as argument and returns Model object in Either, wrapped in a Future.

  2.Repositories:

- abstract class - contains function declarations
- Contract/ defination
- The method takes request object or request parameters as argument.
- Returns Entity class wrapped in Either wrapped in a Future.

  3.Entities:

- Abstraction of a model? - Not abstract class just plain class
- Business objects/ Data structures

---

DATA LAYER:
1.Datasources:

- Source of the data
- Making API rqeuests, caching the data
- abstract class and implementation in same file
- Request file: Contains instance of Request class and Request Parameter class.
  2.Repositories:
- Concrete implementation of repository in the domain layer
- return Right or Left in the methods
- Conatins an instance or object of DataSource class
- That class contains method defination of the abstract method defined in the abstract class.
- The method takes same argument i.e request object or request parameters as that in the domain layer repository function.
- Returns Model class wrapped in Either wrapped in a Future.
- In the function body, call the datasource method and passes all the arguments to the datasource function

  3.Models:

- Business object or data structure
- Child class of entity
- Has super constructor, fromJson(with factory method) and toJson methods.

---

PRESENTATION LAYER:
1.BloC:
2.Pages:
3.Widgets:

- Either<L,R> - Left: Error, Right: Data - used to represent any two types at the same time, so future can be either of type failure or data.
- extends: child class extends a parent class
- implements: concrete class implements an abstract class
- override: the abstract class methods in concrete class - to call a method from a base or parent class
- @override is polymorphism
- what is in angle bracket - type parameters
- super - used by the child class to call parent class constructor and pass it parameters
- to understand the business logic - ask yourself - what does this screen do?

---

TDD: TEST DRIVEN DEVELOPMENT

- seperate test folder with same folder structure as lib.
- write unit test cases: call the methods from each class and pass the dummy mock input to it, verify wheter they return the desired pre defined output
- mockito - mock inputs to test the code
- all files will have same name with suffix \_test.dart
- YAGNI - write test case first and then actual code
- main function - setup,group - test - description, function (to mock)
- Arrange, Act, Assert
- Json files cannel fixtures to inout some dummy data

---

Libraries used and their functions:
1.Service locator: get_it
2.Bloc for state management: flutter_bloc
3.Value equality: equatable - because dart supports on referential equality by default
4.Functional programming thingies: dartz - either
5.Remote API:
i.data_connection_checker_nulls
ii.http
6.Local cache: shared_preferences
