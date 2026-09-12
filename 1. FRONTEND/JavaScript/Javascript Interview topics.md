1. prototypes
2. call, bind, apply
3. closure
4. hoisting
5. promises, async await
6. js engine, event loop

---

Prototypes:

Q1. Explain prototypes in JavaScript?

- Prototype is a mechanism in javascript by which multiple objects can reuse shared logic or behaviour.
- So there is a prototype object which exists on a function and we can add different methods and properties on it.
- And when we create the objects with new, then we can use those methods and properties.
- Modern class syntax in Javascript actually uses this prototype under the hood.
- And thats how inheritance works

Q2. Can you give a code example?

function Person(name) {
this.name = name;
}

Person.prototype.sayHi = function() {
console.log("Hi " + this.name);
};

const p1 = new Person("Pritam");
const p2 = new Person("Neha");

p1.sayHi();
p2.sayHi();

Q3. Whats the difference between .prototype and a***proto***?

Q4. How inheritance works in JavaScript using prototype?

Q5. How is class syntax using prototype behind the scenes?

---

call, bind, apply, this:
