- How to create a custom hook?
- How to create a reusable UI component, maybe from a UI library?
- How to create datatable component and reuse it for list api
- Interview question types - 1.Given code snippet - Find error, 2.Given code snippet - find output
- Common react situation; UI renders before API response in arrived.
- React project - colour constants and string constants for entire project
- Testing react application - Test on all browsers and mobile
- Passing data between components - lifting state up and prop drilling (add prop drilling in notes)

JAVASCRIPT:

- What are default parameters in a javascript function?
- Finding out which elements from one array belong to other array using some object property => Running loop over two arrays - No, Use filter and some

CLOSURE:

**Function nesting** is when a function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed out.

A **closure** is a function that retains access to variables from its **lexical scope** , even after the outer function has finished executing.

---

REACT:

- Concept of default and named import/export
- Named alias for default and named import/export

// Default export
export default function add(a, b) {
return a + b;
}

// Named exports
export function subtract(a, b) {
return a - b;
}

export function multiply(a, b) {
return a \* b;
}

// Import default export with alias
import sum from './mathUtils'; // 'sum' is an alias for the default 'add' function

// Import named exports with and without alias
import { subtract, multiply as times } from './mathUtils';
// 'subtract' is used as-is
// 'multiply' is aliased locally as 'times'

// Usage
console.log(sum(5, 3)); // 8
console.log(subtract(5, 3)); // 2
console.log(times(5, 3)); // 15

import { TextInput as CDSTextInput } from '@carbon/react';

- Important add this: Examples of relative(from reference of the current file) and absolute paths (from root level)

---

https://www.freecodecamp.org/news/learn-typescript-beginners-guide/

Performance:
Use memoization
Debouncing
Lazy loading

Error handling:
Error boundaries
try/catch

Security:
HTTPs

---

const MyComponent = ({ name, ...props }) => { // rest in function signature in argument
return <div {...props}>{name}`</div>`; // Spread the received props onto the div
};

- using rest in the argument and spread inside the component
- used for generic components where any number of props are required

---

Database management tools: (Alternatives to CLI)
1.Mongodb compass
2.DBeaver
3.MySQL workbench
4.Microsoft SQL Server Management Studio (SSMS)

---

Web server: A software that handles http requests and sends response.
1.Apache HTTP Server
2.Nginx
3.Microsoft IIS
4.Express (Node.js)

---

- add: ssh instead of https in git repo
- software lingo: Data corruption in db

---

SHB:
1.Security
2.Authentication and authoraisation:
3.Form validation for lab requisition
4.What is an auth server?

1.An API call is made to EHR to fetch HL7 data of the patient.
2.The HL7 is parsed using a parser.
3.The patient details are populated on the form and rendered to the browser.
4.The user chooses the test and submits form.
5.The form data is collected in backend.

---

JENKINS:

- I have a react application. Its hosted on github. I also have a netlify and jenkins account. I want to craete a pipeline such that when ever i merge something in main branch, it should trigger a build and deploy on netlify. Note: Jenkins server is in AWS EC2

Jenkins script understanding STEPS:

- Change to the root user after logging in
- Add the Jenkins debian repo to the aptitude sources list
- Configure Jenkins and plugins
- Configure nginx
- Update the source lists and upgrade any out of date packages
- Install the software for the Jenkins master: openjdk-11-jdk, nginx
- Then install jenkins
- Confirm that jenkins and nginx are installed
- Retrieve the inital admin password

---

AWS, CLOUD:

- how to ssh into an ec2?
- how to use lambda fn using vs code?
  https://www.cloudskillsboost.google/paths/8
- For bash - https://guide.bash.academy/
- learn shell scripting. required for CICD, Cloud computing etc.
- Kubernetes used for scaling and load balancing containers
- Pub sub

---

RBAC:

- The role and permission is received in the API response for a particular resource.
- Based on the permissions in response, we can show/hide the screens or allow/deny actions to users on a screen.
- Permissions for create, read, update, delete (CRUD) a resource.

---

- Frontend - AI use
- Frontend - How to automate or build a tool or framework to create HTML pages or components, configuration based UI.
- Backend - API - Support should be there for - Search, Sort, Filter, Pagination.
- Backend - API errors - Throw meaningful messages for API errors, send exceptions, error code and relevant message in response.
- Developer testing - Manual testing, automation testing
- UI Tasks - UX Handoff, UI development, API integration, Testing
- Agentic AI
- Vibe codeing: Develop software using AI by just giving prompts and checking
