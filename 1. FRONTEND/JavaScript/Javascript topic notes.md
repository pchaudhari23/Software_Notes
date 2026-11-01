Topics list:

1. References
2. Hoisting
3. Closure
4. Promises, async/await
5. Event loop....
6. Debounce
7. Throttling
8.

---

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

- Hoisting is a JavaScript behavior where declarations of variables and functions are processed before the code execution. It happens during the creation phase, so it appears as if they are moved to the top of their scope.
- Only declarations are hoisted, not initializations. So when var is hoisted, its initialized to undefined.
- What is TDZ? When let and const are hoisted, they are not initialized and if we try to access them we get reference error. The period when they are hoisted but not yet accessible is the Temporal Dead Zone.

---

- Scope: Global scope, Function scope, Block scope. Others are module scope, lexical scope.
- **Function nesting**: Function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed outside.
- If a variable is declared inside a function, its scope is limited to that function, which means it cannot be accessed outside of that function. If it is outside, then it has a global scope; it can be accessed anywhere.
- var is function scoped, let and const are block scoped.

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

- A closure is created when a nested function can still access variables from its outer function's scope, even after the outer function has finished executing.
- Why do we use closures? We use closures to keep the data private, and allow functions to preserve their variable state which is useful for things like callbacks, event handling and memoization.

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

```JavaScript
function createAccount(balance) {
  return {
    deposit: (amt) => (balance += amt),
    getBalance: () => balance,
  };
}
const acc = createAccount(100);
acc.deposit(50);
acc.getBalance(); // 150
acc.balance;      // undefined, balance is inaccessible from outside
```

---

**PROMISES, ASYNC/AWAIT:**

Q1. What are promises in javascript? Promise is an object which acts like a placeholder for the future value of an asynchronous operation. The promise can be in one of 3 states - pending, fulfilled, rejected.

Q2. Can you explain the asynchronous behaviour of Javascript? So javascript is single threaded which means it can do one thing at a time. When it encounters an operation that takes an unpredictable amount of time, like an API call, it does not wait. It passes it to the browser, which executes it separately, and JavaScript continues to the next operation. When the browser finishes, the callback goes into a queue, and the event loop pushes it onto the call stack once the stack is empty. Promise callbacks go in a separate queue that gets priority.

- Use either `async/await` with `try/catch`, or `.then().catch()`.
- `resolve(value)` → the value goes to `.then()`. `reject(error)` → the error goes to `.catch()`.
- With `await`, put the call inside `try`, and handle failures in `catch`.
- Promise utilities: Promise.all, Promise.race
- Always reject with an `Error` object, not a string.
- `await` pauses only that async function until the promise settles. The rest of the program keeps running.
- `.then()` doesn't pause anything. The code after it runs immediately, and the callback fires later when the promise settles.
- Learn how to:
  - Convert an `async/await` function into using `.then().catch()`?
  - Convert `.then().catch()` function into using `async/await`?
  - How to promisify a function?

---

**MISCELLENEOUS:**

Javascript - Dynamically typed - Determines data type of a value at runtime.

Typescript - Statically typed - Determines data type at compile time, preventing errors at runtime.

Strict type checking: === (data type & value), Equality checking: == (only value)

Data types: 1. Primitive, 2. Non primitive

Type coercion - Converting data types from one to other form. String, Numeric, Boolean, Object to primitive coercion

1.Implicit coercion, 2.Explicit coercion/Type casting

ARRAY INTERSECTION: let intersection = arr1.filter(x => arr2.includes(x));

ARRAY DIFFERENCE: let difference = arr1.filter(x => !arr2.includes(x));

- Null check: ?. - checks that something should not be null or undefined. used to fix error - cannot read property of undefined or use an empty array with OR condition (SomedatainArray || [])
- ...args - array of aruguments - rest operator - when it's not known beforehand how many props would be there. In react it's ...props - object of props when number of props is not known

---
