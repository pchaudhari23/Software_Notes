How React works?

- React maintains a **light weight copy** of actual DOM in memory called **virtual DOM**.
- When the application's state or props changes, new virtual DOM is created and compared with the old virtual DOM.
- Then react updates only those parts of real DOM which are changed in the virtual DOM.
- This comparions between old and new virtual DOM is done using something called **diffing algorithm**.
- The process of comparing and updating the real DOM is called **Reconciliation**.
- All this is done to **avoid re-rendering** a real DOM on every change as it is expensive computation.

---

REACT 19 Features:

1. React Compiler:
2. useAPI:
3. New hooks -
4. Actions:

---

Server side rendering

getServerSideProps

Static site generation

getStaticProps

---

mapStateToProps:

mapDispatchToProps:

middlewares:

---
