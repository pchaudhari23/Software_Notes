NODE:

- Javascript **runtime environment** which runs on **Google** **chrome's V8 javascript engine**.
- Executes **outside** the browser.
- **Single threaded**: It executes one main thread sequentially so the code runs line by line.
- **Event loop:** Async tasks are handled by the **event loop** , so the main thread never blocks.
- Has **Non blocking I/O**: Uses **libuv** library to perform I/O operations.
- **Worker threads:** For CPU-heavy tasks, Node.js supports **worker threads** to run JavaScript in **parallel** from a thread pool.
- **Event driven**: Supports **asynchronous code** execution - Uses promises, callbacks and async/await.
- Has **built in modules** for various functionalities - like file handling, encryption, data fetching etc.
- Modules are written in JavaScript & C++ language
- Cross platform, Rich ecosystem, Scalable, real time applications
- Free, open-source
- Current version: v24.x (Dec 2025)

---

EXPRESS:

- Fast, lightweight, minimalist framework
- Buidiling **web applications** and **APIs** with Node js
- Supports **middlewares** to intercept and process requests and responses
- express.json() for JSON and express.static() for serving static files
- Supports **routing**
- Supports templating engines
- RESTful API Development
- Static file serving
- Unopinionated - so we don't have to follow a fixed project structure
- Current version: v5.x (Dec 2025)

---

Nodemon:

---

NVM – Node version manager

- Used to work with multiple node js versions in the system. Useful for testing, debugging, checking new features.
- Download and install exe.
- nvm --version: Check nvm version
- nvm list: List all node js versions
- nvm install 18.20.2 OR nvm install 22.23.1 OR nvm install 24.18.0 : Install specific versions
- nvm use 18.20.2 OR nvm use 22.23.1 OR nvm use 24.18.0 : Use specific version among installed
- nvm install lts: Install latest LTS node
- nvm install latest: Install latest node

Switch versions for projects:

cd my-old-project
nvm use 18.20.2

cd ../my-new-project
nvm use 24.18.0

---

PM2 in node js - Process manager for node applications

---

PACKAGE MANAGER: NPM & YARN

1. Install: npm install `<package-name>`@`<version>`, yarn add `<package-name>`@`<version>`. npm install lodash@^4.0.0, yarn add lodash@^4.0.0 => ^ is used to install version range, - install minor updates and ~ for patches
2. Uninstall: npm uninstall foo, yarn remove foo
3. dev dependencies: --save-dev

---

Debugging node applications in VS Code: Set breakpoints

1. Without launch.json: VS Code toolbar => Run => Start debugging
2. With launch.json: VS code - Side panel => Run and debug => create launch.json file

- What is blocking vs non-blocking code?

---

EXPRESS:

next(), middleware - app.use(), templating engine, static rendering?

Request methods:

- req.body
- req.params
- req.query
- req.method
- req.url
- req.session - used to manage session

Response methods:

- res.send() - send string in response
- res.json() - send json in response
- res.status()
- res.redirect()
- res.render()
- res.set()
- res.cookie()

---

WEB SERVER:

- Computer software installed on server hardware that serves HTTP requests.
- Apache HTTP server: Node
- Apache Tomcat: Java
- IIS (Internet Information Services): Microsoft .NET
- nginx
- WAMP server: PHP
- Web server: A software that handles http requests and sends response. Eg: Apache HTTP Server, Nginx, Microsoft IIS, Express (Node.js)

---

NOTES: Software notes - Backend, Database

PERSONAL PROJECTS:

1. Invoice manager
2. Products typescript
3. Students report - MVC

What can I do now?

1. Create REST API
2. Write CRUD queries
3. Implement layered architecture

My Backend knowledge:

1. invoice manager
2. medconnect
3. students report
4. product typescript
5. node concurrent
6. mongo query
7. node learning
8. my notes

---

- File upload to AWS S3

---

Node JS:

1. Introduction and basic javascript
2. Node JS basic concepts and installation
3. Node JS module system
4. File system and command line arguments
5. Asynchronous Node JS, Promises, async await in Node JS
6. Web servers: Express JS
7. Accessing an API from browser
8. Routing in node applications
9. REST APIs
10. Working with dynamic content & adding templating engines
11. The Model View Controller (MVC)
12. SQL introduction
13. Understanding sequalize
14. Working with NoSQL & using Mongo DB
15. Working with Mongoose
16. Authentication and security in node applications
17. Understanding validation
18. Error handling
19. Sorting, Pagination and Filtering
20. File upload & download
21. Sending emails
22. Realtime web applications, websockets & socket.io
23. Payments in node applications
24. Sessions & cookies
25. Working with GraphQL
26. Node JS as a build tool & using npm
27. Modern Javascript & node JS
28. Node JS & typescript
29. Introduction to Deno
30. Deno, CRUD & Databases (MongoDB)
31. Debugging node applications
32. Testing node applications
33. Deploying node applications

---

Libraries:

1. express
2. express-validator
3. express-session
4. express-handlebars
5. ejs
6. pug
7. bcrypt
8. jsonwebtoken
9. nodemon
10. multer
11. mongodb
12. mongoose
13. connect-mongodb-session
14. mysql2
15. sequalize
16. nodemailer
17. nodemailer-sendgrid-transport
18. socket.io
19. socket.io-client
20. body-parser
21. csurf
22. connect-flash
23. pdfkit
24. stripe
25. helmet
26. compression
27. morgan
28. graphql
29. express-graphql
30. mocha (testing)
31. chai (testing)
32. sinon (testing)
33. typescript
34. @types/node
35. @types/express
36. @types/body-parser
37. chalk
38. validator
39. request

---
