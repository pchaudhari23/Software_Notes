MODULE SYSTEM:
1.Common JS:
const fs = require('fs')

const someFunction = () => {}

module.exports = someFunction;

#Name exports in common js:
named imports:
const myModule = require('./module'); // Importing the entire module

named exports:
module.exports = {
function1: someFunction1(),
function2: someFunction2(),
}

---

2.Module JS:
import fs from "node:fs"

const someFunction = () => {}

export default someFunction;

#Name exports in module js:
named imports: import {..., ....} from "..."
named exports: export default {...., .....} <-- Used when multiple functions are defined in single file.

- Use a type: 'commonjs' or type: 'module' in package.json. commonjs type is default

---
