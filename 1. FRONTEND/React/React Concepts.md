REACT:

- Javascript library for building user interface.
- React maintains a **lightweight copy** of the actual DOM in memory called the **virtual DOM**.
- When state or props of UI components change, React creates a new virtual DOM and compares it with the old DOM using a **diffing algorithm** to identify changes.
- Then react updates only the changed parts of the real DOM. This process of comparing and updating the real DOM based on these changes is called **reconciliation**.
- This **minimizes re-rendering**. So when there are frequent DOM manipulations they happen in memory and only minimal updates are applied to the browser's actual DOM.
- Latest version: v19.2 (Dec 2025)

---

FEATURES:

- Virtual DOM
- JSX - It stands for Javascript XML is a HTML like syntax which can be used to do javascript programming.
- Reusable components
- Data flow: It has one way data flow which is from parent component to child components via props. Passing data between components - lifting state up and prop drilling
- Hooks: React hooks is another major functionality
- Server components: It provides some server components and can be used for serverside rendering.
- Serverside rendering: It's a process in which the page renders on the server and the HTML code is sent to the client. It decreases the loading time of the page.
- Compatibility: It can be easily use with other technologies like Express, Node for MERN stack
- SEO: It can help increase the website ranking for SEO.

---

CORE CONCEPTS:

1. **State:**

   - State is the data which a react component holds.
   - Local state: usestate hook, Global state: state management libraries like redux.
   - State variables must not be mutated or updated directly. First create a copy and then modify.
   - Usually state variable of a parent component acts as a prop for child component.

2. **Props:**

   - Props are the attributes or arguments passed to a react component.
   - Props are read only, their value must not be changed.

3. **Hooks:**

   - Hooks are the inbuilt functions in react which we can use for acessing and modifying the state variable or do various operations throughout a components lifecycle.

4. **Virtual DOM & Reconciliation:**

   - React uses a virtual DOM to compare changes in memory and updates only the necessary parts of the real DOM through reconciliation, minimizing re-renders and improving performance.

5. **Webpack bundler:**

   - Bundler is a tool which takes all the javascript files and all the code in the project and creates single individual html, css, js files in form of static assets which the browser uses to display the website.
   - Webpack is a type of bundler which react uses.

6. **Babel:**

   - Babel is a javascript compiler which transforms or compiles the javascript code in such a version that all the browsers can understand it. It makes advanced javascript code compatible with older browsers.

---

COMPONENTS:

**Functional component:**

- Functional components are simple javascript functions.
- State management: Functions components use useState hook and state variable.
- Lifecycle: Function components use hooks for operation. It uses useEffect hook for component mounting and unmounting.
- No constructor or this keyword, props as argument to function.
- Syntax wise functional components are easier to learn and fast to implement.

**Class component:**

- Class components are ES6 classes which extend React components library and it has a render method.
- State management: Class components use state objects to store state of component and they use this.state and this.setState method.
- Lifecycle: Class components use lifecycle methods. It uses componentDidMount, componentDidUpdate and componentWillUnount.
- Class components use a constructor and this keyword and access props using this.props.
- Also class components are outdated now. The new react documentation does not mention them. They are only used in legacy codebases now.

**HOC:**

- It is a way to enhance a component.
- So its a function which takes a component as an input and gives enhanced component as its output, without modifying or changing the original component.
- It does not modify the original component.HOC is a pure function.
- The argument is typically called WrappedComponent because it refers to the component that is being "wrapped" by the Higher-Order Component (HOC).

---

REACT 19:

1. React compiler - no useMemo, no useCallback
2. Server actions
3. Its own web components and better efficient asset loading in background
4. useAPI
5. New hooks

---

React Starting point:

```javascript
// React <= 17:
import ReactDOM from "react-dom";

ReactDOM.render(<App />, document.getElementById("root"));

OR;
// React 18+
import { createRoot } from "react-dom/client";

const rootElement = document.getElementById("root");
const root = ReactDOM.createRoot(rootElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

HTML: <div id="root"></div>;
```

- Components: Dumb but reusable, gets data from prop & displays it.
- Container: Smart - state management, data fetching, contains business logic.

---

```javascript
// rest in function signature in argument
const MyComponent = ({ name, ...props }) => {
  return <div {...props}>{name}</div>; // Spread the received props onto the div
};
```

- using rest in the argument and spread inside the component
- used for generic components where any number of props are required
- prop types & default props

---

REDUX: mapStateToProps, mapDispatchToProps

---

BOILERPLATE TEMPLATES:

- https://github.com/react-boilerplate/react-boilerplate
- React Boilerplate CRA Template:https://cansahin.gitbook.io/react-boilerplate-cra-template/
- Create React App: https://create-react-app.dev/

---

- Project - npm create vite@latest
- Testing - @testing-library/react and jest
- Building - npm run build - dist or build folder
- Deployment - manual upload folder or deploy from a git repo

---
