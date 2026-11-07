JAVASCRIPT ENGINE: Execute JavaScript programs

- Chrome, Microsoft Edge - V8
- Firefox - SpiderMonkey
- Apple Safari - JavaScriptCore/Nitro
- Internet Explorer - Chakra

---

COMPILATION:

1. Parsing: Source code is parsed and converted into AST (Abstract Syntax Tree).
2. Bytecode Generation: The AST is used to generate bytecode (an intermediate representation).
3. Interpretation: The bytecode is executed line by line by the engine.
4. JIT Compilation: Frequently executed code/ hot code is optimized and compiled into machine code using Just-In-Time (JIT) compilation. This improves performance.
5. Execution: Synchronous code is executed immediately and event loop manages the order of execution for async code. JavaScript engine has a call stack, two queues and a heap.

---

COMPONENTS:

1. Call stack: Executes synchronous function calls.
2. Microtask queue: High priority asynchronous task - Promises, then & catch, async & await, fetch (returns a promise immediately with pending state, then or catch goes into microtasks after the promise is resolved).
3. Macrotask queue/Task queue: Low priority asynchronous task - Web API (Browser), setTimeout, setInterval, DOM events (click, scroll etc.), I/O events, setImmediate (Node.js API).
4. Heap: Memory area where JavaScript stores dynamically allocated data. Stores objects, arrays, functions, closure, class instance etc and is managed by garbage collector.

---

EXECUTION CONTEXT:

- It is the runtime environment in which JavaScript code is executed.
- Execution context is stored in call stack. Each function call creates a new execution context which is pushed on top of stack. After it is finished, the context is popped out of stack.
- Async tasks wait in queue.
- Reference data such arrays, objects, functions are stored on heap.
- There are two phases of execution: 1. Creation phase, 2. Execution phase.
- Creation phase: Memory allocated for functions and variables, this binding decided, hoisting, scope chain building happens here.
- Execution phase: Code runs line by line, values assigned, functions executed.

---

EVENT LOOP:

1. Execute all synchronous code first in the call stack until it’s empty
2. Execute all microtasks (drain the microtask queue completely)
3. Execute only one macrotask - handled by browser/web API
4. After each macrotask, check and run all microtasks again before the next macrotask
5. Repeat

---

CODE:

```javascript
console.log(1); // synchronous code

setTimeout(() => {
  console.log(2); // macrotask queue
}, 0);

Promise.resolve().then(() => {
  console.log(3); // microtask queue
});

console.log(4); // synchronous code
```

OUTPUT: 1 4 3 2

---

PARALLEL EXECUTION:

- JavaScript is single-threaded: only one piece of JavaScript runs at a time per runtime.
- Asynchronous operations are queued, and the event loop co-ordinates the callback execution.
- Async work itself (timers, network, I/O, crypto, etc.) is handled outside JavaScript’s main thread by the browser/Node runtime or OS.

Browser: Web workers - allow true parallel execution of JavaScript.

- Each thread is its own JavaScript runtime having their own call stack, task queues (microtask & macrotask), heap and event loop.
- Communicates with main thread via message passing (postMessage).
- Cannot access DOM directly.

Node.js: Worker threads - provide parallel execution for CPU-heavy tasks.

- Each thread is its own JavaScript runtime having their own call stack, task queues (microtask & macrotask), heap and event loop.
- Libuv has 4 threads in thread pool by default.
- Communicates via message channels (parentPort, postMessage).
- Can share memory explicitly via SharedArrayBuffer.
- Node also uses libuv’s thread pool for async I/O (file system, DNS, crypto), but those threads don’t run JavaScript — they just handle background work.

---
