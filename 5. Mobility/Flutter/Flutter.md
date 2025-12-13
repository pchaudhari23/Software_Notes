FLUTTER:

- Flutter is an **open source SDK** developed by **Google**.
- Used to build **natively compiled** applications (compiled to **ARM,** **x86** and **JavaScript** for the web).
- Used to develop **multi platform applications**: Mostly mobile applications but also web, desktop and embedded application.
- It uses **Dart programming language** and **single code base** is used for developing applications.
- It allows **fast development** due to **hot reload** and **hot restart** features.
- It offers **high performance** due to its **Impeller rendering engine** and **Ahead of time compilation**.
- Provides rich and beautiful widgets for ui - **Material Design widgets** (Android-style) and **Cupertino widgets** (iOS-style).
- It has **rich ecosystem** where **pub.dev** provides lots of **plugins and packages**.
- Current version: v3.x (Dec 2025).

---

DART:

- **Dart** is a **open source**, **object-oriented programming language** created by **Google.**
- Its used to build **fast, scalable apps** for **multiple platforms** like mobile, desktop and web. Mainly used in **Flutter**.
- Syntax is similar to **C++, C#, Java**.
- **Strongly typed**, with **type inference** (var), and optional dynamic typing.
- **Null safety** — eliminates null reference errors with compile-time checks.
- **Asynchronous programming** using: **async/await, Futures, Streams**
- **Garbage collected** , memory-managed language.
- Supports **JIT compilation** during **development**. So dart code is compiled on the fly using Dart VM making the hot reload possible.
- Supports **AOT compilation** in **production build** to compile to native machine code for maximum performance.
- Current version: v3.x (Dec 2025).

---

Android studio:
SDK Manager - Android SDKs
AVD Manager - Android Virtual Devices

---

Flutter CLI commands:

- flutter create <project_name>
- flutter pub add <package_name>: add a new dependency
- flutter pub get: get all dependencies in pubspec file
- flutter pub upgrade: upgrade all the dependencies in pubspec file
- flutter doctor
- flutter run

---

VS Code: Must have extensions:

1. Dart
2. Flutter
3. dart-import
4. bloc
5. Flutter Feature Scaffolding

- Dependencies tab in vscode to explore installed libraries.
- dart imports package: Run the command "Fix Imports" from the Command Palette. All imports from your own package will become relative. Also, the "Organize Import" command will be called. Seperates our imports from pacakge imports.
- Flutter application: to share or take backup - create a zip file excluding build folder. Same for commiting to git.

---

FLUTTER TOPICS:

1. UI - Widgets, Responsive & adaptive UI, animations
2. Future builder, Listview builder, Gridview builder
3. Routing and navigation
4. State management - Providers package, RiverPod
5. State management - BLoC Pattern
6. Clean Architecture
7. User input, form handling and validation
8. Asynchronous programming - Future, Stream, async/await, yeild, Either, fold
9. HTTP Requests, API call, getting and sending JSON data to API and handling local JSON files
10. User Authentication and authorisation
11. Native device features: - Camera, - Maps, - Location, - Internal local database (SQLite), - Communicating with the device using native languages (JAVA, Kotlin, Objective C, Swift)
12. CRUD operations
13. Using Firebase, push notifications : Backend as a service - Firebase authentication - Firebase Firestore - Firebase Cloud Firestore - database (other db is realtime database) - Firebase Cloud Messaging (FCM) - Push notifications - Firebase Cloud Functions
14. Unit testing
15. Debugging & testing on real devices

---

1. main => runApp => MyApp => return MaterialApp => home => Homepage widget
   OR main => runApp => return MaterialApp => home => Homepage widget (lean - one less MyApp widget)
2. Page widget => Scaffold => appbar, body

---

Widget name - Camel case, widget files - seperate multiple words with \_(underscore)
MaterialApp - routes, onGenerateRoute, push, pushNamed

---

Snippets:
Widgets: Stateless & Stateful

- build method is used to build or create the widget at runtime.

class MyWidget extends StatelessWidget {

// constructor
const MyWidget({super.key});

@override
Widget build(BuildContext context) {
return const Placeholder(); // OR maybe Scaffold Widget
}
}

---

class MyWidget extends StatefulWidget {

// constructor
const MyWidget({super.key});

@override
State `<MyWidget>` createState() {
return \_MyWidgetState();
}
OR

@override
State `<MyWidget>` createState() => \_MyWidgetState();
}

class \_MyWidgetState extends State `<MyWidget>` {

int \_stateVariable = 0;

// initialisation method, runs before the build method
@override
void initState() {
super.initState();
}

// takes anonymous function as input, state varaiables mentioned in the state class are changed in the
// setState method's anonymous function. setState method triggers the build method again and the widget
// re-renders, UI update happens

setState(() {});

    @override
    void dispose() {
    	// Clean up the controller when the widget is disposed.
    	_exampleController.dispose();
    	super.dispose();
    }

@override
Widget build(BuildContext context) {
return const Placeholder();
}
}

---

Packages:

---

Shortcut:
in the file - type:

1. stless: for creating stateless widget
2. stful: for creating stateful widget
3. hover on state class and press cntrl . - convert a stateless widget to stateful
   Flutter - dev tools - open in a web browser

---

Questions:

1. What system configurations are required?
2. How to create a build?
3. How is it published on app store or playstore?
4. How to connect with backend?

---

- Learn web development with flutter as well
