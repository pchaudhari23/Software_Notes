1. Hoisting

- It is a mechanism in which javascript moves all the function and variable declarations at the top of the scope before executing them
- If a variable is declared inside a function, its scope is limited to that function which means it cannot be accessed outside that function. If it is outside then it has global scope, it can be accessed anywhere
- var is function scoped, let and const are block scoped
- It doesnt work with let and const. It will give error that this is initialized before being declared

hoist();

function hoist() {
console.log('In hoist');
console.log(x);
var x = 2;
}

console.log(y);
var y = 5;

function hoist2() {
console.log(a);
var a = 'Hello';
}
hoist2();

---

2. Closures

function outer() {
var x = 2;
function inner() {
console.log(x)
}
inner()
}

outer()

---

3. Memoisation, useMemo, useCallback, lazy loading, suspense

- React.memo (for components) - higher-order component (HOC)
- useMemo (for values or computations within a component)
- useCallback (to memoize functions within a component)
- React compiler in react19

---

4. HOCs

- It is a way to enhance a component.
- So its a function which takes a component as an input and gives enhanced component as its output, without modifying or changing the original component.
- It does not modify the original component.HOC is a pure function.
  Yes, the argument is typically called WrappedComponent because it refers to the component that is being "wrapped" by the Higher-Order Component (HOC).

---

5. Error boundry, error handling in React

- class
- functions
- library

---
