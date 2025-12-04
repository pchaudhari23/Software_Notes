REACT:

1. How to create a custom hook?
2. How to create a reusable UI component, maybe from a UI library?
3. How to create datatable component and reuse it for list api

- Interview question types - 1.Given code snippet - Find error, 2.Given code snippet - find output
- Common react situation; UI renders before API response in arrived.
- React project - colour constants and string constants for entire project
- Testing react application - Test on all browsers and mobile
- Passing data between components - lifting state up and prop drilling (add prop drilling in notes)
- Frequently asked javascript and react code interview questions - Type: Spot error, tell output - check with chatgpt

---

const MyComponent = ({ name, ...props }) => { // rest in function signature in argument
return <div {...props}>{name}</div>; // Spread the received props onto the div
};

- using rest in the argument and spread inside the component
- used for generic components where any number of props are required
- prop types & default props

---

JAVASCRIPT:

- What are default parameters in a javascript function?
- Finding out which elements from one array belong to other array using some object property => Running loop over two arrays - No, Use filter and some

CLOSURE:

**Function nesting** is when a function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed out.

A **closure** is a function that retains access to variables from its **lexical scope** , even after the outer function has finished executing.

---
