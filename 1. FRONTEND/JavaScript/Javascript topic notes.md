**TYPESCRIPT:**

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

**REFERENCES**:

- In C or C++, pointers are used to show memory location of data. But in JavaScript, we cannot see the exact memory location of objects, arrays or primitives. This is because JavScript is a high level programming language and memory management is abstracted away from user.
- When we use = sign, we basically give a new name for array or object.

Example:

1. Object:

```JavaScript
// Object
const obj1 = { name: "Adam" };
const obj2 = obj1;

console.log(obj1 === obj2); // true → same reference
obj2.name = "Noah";
console.log(obj1.name);     // "Noah" → proves same underlying object
```

2. Array:

```JavaScript
const arr1 = [1, 2, 3];
const arr2 = arr1;

arr2.push(4);

console.log(arr1); // [1, 2, 3, 4]
console.log(arr2); // [1, 2, 3, 4]
console.log(arr1 === arr2); // true
```

- We can prove the sameness with **reference equality** (`===`) and by observing **shared mutations**.
- But the referential equality applies to arrays and objects only, not primitives. For primitive data types, new copy gets created.
- Primitives are copied by value, objects are copied by reference.

Example:

```JavaScript
let x = 10;
let y = x; // copy, not reference
y = 20;

console.log(x); // 10
console.log(y); // 20
```

---

**this:**

- this is a keyword which gives reference to the object which is currently used in the function's execution context.
- It depends on how the function is called not just where its defined.
- call, bind and apply are use to set the value of this.

**call:**

- takes comma separated arguments
- sets the value of this and executes immediately

**apply:**

- takes array of arguments
- sets the value of this and executes immediately

**bind:**

- takes comma separated arguments
- sets the value of this and returns a function to execute later

Example:

```JavaScript
function greet(place, occasion) {
  console.log(`Hello ${this.name}, welcome to ${place} for the ${occasion}`);
}

const user = {
  name: "Adam",
  sayHi: function () {
    console.log(`Hi, I am ${this.name}`);
  }
};

user.sayHi(); // Hi, I am Adam → this = user

// call → arguments passed individually + executes immediately
greet.call(user, "Pune", "Tech Summit");

// apply → arguments passed as an array + executes immediately
greet.apply(user, ["Mumbai", "Product Launch"]);

// bind → arguments passed individually + returns a new function
const boundGreet = greet.bind(user, "Delhi", "Annual Conference");

boundGreet(); // executes later
```

Question: Why this does not work with arrow functions?

- Normal functions get the value of this from where the function gets called.
- Arrow functions do not have their own this, they inherit it from surrounding scope, as in where the function is defined.

---

**PROTOTYPES**:

Key points:

- In JavaScript everything apart from primitive datatypes - object, array and even function is an object.
- Objects can be created using { } but then they cannot share logic. Functions which are created without new don't create any object.
- Objects can be created by constructor functions using new.

Q1. Explain prototypes in JavaScript?

- Prototype is a mechanism in javascript by which multiple objects can reuse shared logic and they can also inherit features from other objects.
- When we create an object using a constructor function with new, that object gets a link to the constructor's prototype object.
- We can add different methods and properties on the prototype.

Q2. Can you give a code example?

```JavaScript
function Person(name,age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greetUser = function () {
  console.log(`Welcome ${this.name}`)
}

const p1 = new Person('Adam', 25);
const p2 = new Person('Noah', 15);

p1.greetUser();
p2.greetUser();
```

Q3. Whats the difference between .prototype and \_ _ proto _ \_?

- prototype is a property which exists on constructor function.
- \_ _ proto _ \_ is a property which exists on new object which is created.

Example:

```JavaScript
console.log(Person.prototype === p1.__proto__) // true
```

Q4. How inheritance works in JavaScript using prototype?

```JavaScript
function Animal(name, color) {
  this.name = name;
  this.color = color;
}

Animal.prototype.eat = function () {
  console.log(`${this.name} is eating`);
};


function Horse(name, color) {
  Animal.call(this, name, color);
}

Horse.prototype = Object.create(Animal.prototype);

Horse.prototype.run = function () {
  console.log(`${this.name} is running`);
};


const horse1 = new Horse("Thunder", "Brown");

console.log(horse1.name);  // Thunder
console.log(horse1.color); // Brown

horse1.eat(); // Thunder is eating
horse1.run(); // Thunder is running
```

Q5. How is class syntax using prototype behind the scenes?

```JavaScript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greetUser() {
    console.log(`Welcome ${this.name}`);
  }
}

const p = new Person("Adam", 25);
```

---

**HOISTING:**

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

**CLOSURE:**

- **Function nesting**: Function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed outside.
- **Closure:** When the inner function is returned or used outside the outer function, allowing it to remember and access the outer function’s variables even after execution ends.
- Scope: Global scope, function scope, block scope

Example:

```JavaScript
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

**PROMISES, ASYNC/AWAIT:**

- There should be either async/await with try/catch OR .then().catch()
- Using both together is unnecessary even if technically not wrong.
- then called on promise resolve, catch called on promise reject
- Whatever is passed in resolve() - it is collected in then() method
- Whatever is passed in reject() - it is collected in catch() method
- await keyword in the async/ await function stops the function exceution until the code in front of await(eg: fetching data from api) is completed. Once we have the response data, the furthur code is executed.
- .then() and .catch() - chain methods don't stop until the data from api is received. they continue the code after that and whenever the response is received, they will store or set the received data in variable
- make a habit to write all the code in try catch blocks
- make the await api call in the try block
- Usually throw Error class object in a Promise reject
- Promise.all, Promise.race????
- Learn how to:
  - Convert an async/await function into using .then().catch()
  - Convert .then().catch() function into using async/await
  - How to promisify a function

---

**MISCELLENEOUS:**

ARRAY INTERSECTION: let intersection = arr1.filter(x => arr2.includes(x));
ARRAY DIFFERENCE: let difference = arr1.filter(x => !arr2.includes(x));

- == vs === (equality and type checking)
- Type coercion in javascript
- Type casting - converting an object of one datatype into another
- Null check: ?. - checks that something should not be null or undefined. used to fix error - cannot read property of undefined or use an empty array with OR condition (SomedatainArray || [])
- ...args - array of aruguments - rest operator - when it's not known beforehand how many props would be there. In react it's ...props - object of props when number of props is not known

---
