TYPESCRIPT:

- **TypeScript** is an **open-source programming language** developed by **Microsoft** and its **superset of JavaScript**.
- It offers **static typing**, so we explicitly declare data type which helps catch errors **before running the code**.
- **Type inference** helps automatically determine data type if not declared.
- **Interfaces** & **Type alias** helps to define the structure of objects and ensure consistency.
- **Object-Oriented Programming Support**: Classes, inheritance, access modifiers (public, private, protected), abstract classes.
- **Compile-Time Error Checking,** not at runtime.
- Modern JavaScript Support (ES6+) and excellent tooling and IDE support, Intellisense.
- It is compiled into **(transpiled)** into plain JavaScript using typescript compiler which browsers and JavaScript engines understand.
- TypeScript configuration of a project is stored in tsconfig.json file. Compilation: .ts (TypeScript file) => tsc (tsc compiler) => .js (JavaScript file)
- Current version: v5.9 (Dec 2025)

---

HOISTING:

- Hoisting is a JavaScript behavior where declarations of variables and functions are processed before code execution. During the memory allocation (creation phase), JavaScript allocates memory for variables and functions before executing the code.
- If a variable is declared inside a function, its scope is limited to that function, which means it cannot be accessed outside of that function. If it is outside, then it has a global scope; it can be accessed anywhere.
- var is function scoped, let and const are block scoped.
- Only declarations are hoisted, not initializations.
- var variables are hoisted and initialized with undefined.
- let and const variables are hoisted but not initialized.
- Hoisting does work with let and const, but they are placed in the Temporal Dead Zone (TDZ). The Temporal Dead Zone (TDZ) is the time between the start of a scope and the declaration of a let or const variable, during which accessing it throws a ReferenceError. Accessing them before their declaration results in a ReferenceError (not undefined).

```javascript
1.var
	console.log(a);
	var a = 10;
	Output: undefined

2.let/const
	console.log(b);
	let b = 20;
	Output: ReferenceError: Cannot access 'b' before initialization

3.Function declaration hoisting
	sayHello();

	function sayHello() {
 		console.log("Hello");
	}
	Output: Hello

4.Function expression with var
	sayHi();

	var sayHi = function () {
 		console.log("Hi");
	};
	Output: TypeError: sayHi is not a function

5.Block scope (let)
	{
 		console.log(x);
 		let x = 5;
	}

	Output: ReferenceError
```

---

CLOSURE:

- **Function nesting**: Function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed outside.
- **Closure:** When the inner function is returned or used outside the outer function, allowing it to remember and access the outer function’s variables even after execution ends.

```javascript
function outer() {
  let count = 0; // variable in lexical scope

  return function inner() {
    count++; // inner remembers `count`
    console.log(count);
  };
}

const counter = outer(); // outer() has finished executing

counter(); // 1
counter(); // 2
counter(); // 3
```

---

PROMISES, ASYNC/AWAIT:

* There should be either async/await with try/catch OR .then().catch()
* Using both together is unnecessary even if technically not wrong.
* then called on promise resolve, catch called on promise reject
* Whatever is passed in resolve() - it is collected in then() method
* Whatever is passed in reject() - it is collected in catch() method
* await keyword in the async/ await function stops the function exceution until the code in front of await(eg: fetching data from api) is completed. Once we have the response data, the furthur code is executed.
* .then() and .catch() - chain methods don't stop until the data from api is received. they continue the code after that and whenever the response is received, they will store or set the received data in variable
* make a habit to write all the code in try catch blocks
* make the await api call in the try block
* Usually throw Error class object in a Promise reject
* Promise.all, Promise.race????
* Learn how to:
  * Convert an async/await function into using .then().catch()
  * Convert .then().catch() function into using async/await
  * How to promisify a function

---

* Javascript playground: https://playcode.io/
* Typescript: https://www.freecodecamp.org/news/learn-typescript-beginners-guide/

Instead of many if else: use
i.Ternary Operators
ii.Switch Statements
iii.Logical Operators (&& and ||)
iv.Lookup Maps

Lookup maps/lookup object: Eg:

```javascript
function checkBestStudent(subject) {
  var bestStudent = "";

  var lookup = {
    maths: "Adams Milner",
    english: "Akande Olalekan Toheeb",
    chemistry: "Chicago",
    physics: "Denver",
    biology: "Easy",
  };

  bestStudent = lookup[subject];
  console.log(bestStudent);
}

checkBestStudent("maths");
```

---

- Implement a loop counter to avoid getting stuck into infinite loop. On exceeding a count number, take an action to break and come out of loop.
- Store all the strings in a constants file and use constants wherever required.
- Finding out which elements from one array belong to other array using some object property => Running loop over two arrays - No, Use filter and some

---

Use spread operator to copy an object or to duplicate it and manipulate it.

var obj1 = {'key1':'val1', 'key2':'val2'}
var obj2 = {...obj1}
obj2 //{key1: 'val1', key2: 'val2'}

---

Javascript object keys could be in quotes or without quotes.
{
"PageSize": pageSize,
"PageCount": pageCount
}
OR
{
PageSize: pageSize,
PageCount: pageCount
}
if key and value both are same, then shorthand expression - use only one word for both.
{
pageSize: pageSize,
}
could be
{
pageSize
}

---

ARRAY INTERSECTION: let intersection = arr1.filter(x => arr2.includes(x));
ARRAY DIFFERENCE: let difference = arr1.filter(x => !arr2.includes(x));

---

- The this keyword is used to get/access or to set/modify/assign a value to the data member variable of a class, in that class itself.
- The scope of this keyword to be used on a data memberis in that particular class.
- this keyword is used on the data member of a class and not on the member function.

Eg:
class Customer{
int customerID;

    void setCustomerID(int ID){
    	this.customerID = ID;
    }

}

---

JSON:
JSON.stringify(Javascript Object) - Convert a JS Object to string
JSON.parse(JSON String) - Convert a JSON String to JS Object
toString(), parseInt(), parseFloat()

---

HTML String:

HTML Document:

1. HTML DOM => HTML String
2. HTML String => HTML DOM
   const parser = new DOMParser();
   var HTMLDocumentDOM = parser.parseFromString(htmlString, "text/html");

To make base64 of an HTML file:
1.Get the string representation of that html file - using DOMParser (its used to create a DOM from any string)
2.Covert that string to base64 - using btoa()

---

BASE 64:

- Encoded format of PDF, image, HTML page etc in the form of long string of characters.
- Binary string: A representation of a file format (Eg: HTML, PDF, Image etc.) as a string of binary numbers.
- Any media type with any extension can be converted to base64 and vice versa.
- File <=> Binary string <=> Base64 <=> File

btoa() - Binary string to Base 64
atob() - Base 64 to Binary string

BLOB file type??

base64 to blob - new Blob()
base64 to file - new File()

---

Type check: ===
Null check: ?. - checks that something should not be null or undefined. used to fix error - cannot read property of undefined or use an empty array with OR condition (SomedatainArray || [])

- ...args - array of aruguments - rest operator - when it's not known beforehand how many props would be there. In react it's ...props - object of props when number of props is not known

---

Query parameters:

- Occurs in the url after the domain name. Starts with a ? and seperated key value pairs by &
  Eg: localhost:3000?name=John&surname=Watson&age=25
  query parameters - started in the url after ? and parameters are seperated by &
  query parameters in above example are, name, surname and age

Path parameters:

- Occurs in the url path. Mentioned in curly braces in url path
- Eg: getdata/{product}/{id}

URL string functions:

1. window.location.href - gives URL
2. window.location.pathname - path of URL
3. window.location.search - query string parameters

---

Modelling - we need to define datatype explicitly in typescript. Javascript infers datatype automatically.

- Create objects using Model class in models folder
- Create datatypes using interfaces in types folder
  Creating type interfaces will give type safety.
  Type safety means the is no need to use generics datatype like Object or any or base datatype` but specific datatype eg: Customer object
- Entity: Business object. It's what we see in UI, what we send through API and store in DB. Entities are related to each other. Hence ER diagrams. Eg: Social media app: Post, Comment, User etc., Ecommerce app: Product, Cart, Orders, User etc.

---
