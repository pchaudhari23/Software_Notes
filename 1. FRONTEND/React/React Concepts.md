TOPICS:

- Data fetching: Axios, Tanstack query
- Forms: Formik and Yup, React form hook
- State management: Redux, Zustand
- Unit test: testing-library/react, Jest
- Sanity test: Cucumber, playwright
- React flow
- Isomorphic react

---

FEATURES:

- Virtual DOM
- JSX - It stands for Javascript XML is a HTML like syntax which can be used to do javascript programming.
- Reusable components
- Data flow: It has one way data flow which is from parent componet to child components via props
- Hooks: React hooks is another major functionality
- Server components: It provides some server components and can be used for serverside rendering.
- Serverside rendering: It's a process in which the page renders on the server and the HTML code is sent to the client. It decreases the loading time of the page.
- Compatibility: It can be easily use with other technologies like Express, Node for MERN stack
- SEO: It can help increase the website ranking for SEO.

---

CORE CONCEPTS: 1. State:

- State is the data which a react component holds.
- Local state: usestate hook, Global state: state management libraries like redux.
- State variables must not be mutated or updated directly. First create a copy and then modify.
- Usually state variable of a parent component acts as a prop for child component.

  2.Props:

- Props are the attributes or arguments passed to a react component.
- Props are read only, their value must not be changed.

  3.Hooks:

- Hooks are the inbuilt functions in react which we can use for acessing and modifying the state variable or do various operations throughout a components lifecycle.

  4.Virtual DOM & Reconciliation:

- A website works by DOM manipulations and if there are frequent updates to the UI, then web application can become slow or inefficient. Performance is affected.
- So React stores a copy of the DOM elements in the memory known as virtual DOM.
- So whenever any change happens in the UI, React creates a new copy of the virtual DOM.
- Then it compares the new virtual DOM with the old one to find out what changes happened. This is called as diffing.
- All this process happens in the memory, nothing is yet painted on the browser screen.
- Then it makes the changes of only updated UI nodes in the real DOM with minimum possible steps. This process is reconciliation.

  5.Webpack bundler:

- Bundler is a tool which takes all the javascript files and all the code in the project and creates single individual html, css, js files in form of static assets which the browser uses to display the website.
- Webpack is a type of bundler which react uses.
- Babel is a javascript compiler which transforms or compiles the javascript code in such a version that all the browsers can understand it. It makes advanced javascript code compatible with older browsers.

---

Components:-

Functional component:

- Functional components are simple javascript functions.
- State management: Functions components use useState hook and state variable.
- Lifecycle: Function components use hooks for operation. It uses useEffect hook for component mounting and unmounting.
- No constructor or this keyword, props as argument to function.
- Syntax wise functional components are easier to learn and fast to implement.

Class component:

- Class components are ES6 classes which extend React components library and it has a render method.
- State management: Class components use state objects to store state of component and they use this.state and this.setState method.
- Lifecycle: Class components use lifecycle methods. It uses componentDidMount, componentDidUpdate and componentWillUnount.
- Class components use a constructor and this keyword and access props using this.props.
- Also class components are outdated now. The new react documentation does not mention them. They are only used in legacy codebases now.

---

Zustand:

- It is a small and fast state management library which is an alternative to redux.
- It uses very basic API without any boilerplate which makes it preffered over redux.
- It uses hooks for state management.

---

BOILERPLATE TEMPLATES:

1.https://github.com/react-boilerplate/react-boilerplate
2.React Boilerplate CRA Template:https://cansahin.gitbook.io/react-boilerplate-cra-template/
3.Create React App: https://create-react-app.dev/

---

1.Project - npm create vite@latest
2.Testing - @testing-library/react and jest
3.Building - npm run build - dist or build folder
4.Deployment - manual upload folder or deploy from a git repo

---

React 19 features:
1.React compiler - no useMemo, no useCallback
2.Server actions
3.Its own web components and better efficient assest loading in background

---
