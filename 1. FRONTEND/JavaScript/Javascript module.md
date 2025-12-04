COMMON JS:

```javascript
const fs = require("fs");

const someFunction = () => {};

module.exports = someFunction;
```

Named Import:

```javascript
const myModule = require("./module"); // Importing the entire module
```

Named Export:

```javascript
module.exports = {
  function1: someFunction1(),
  function2: someFunction2(),
};
```

---

MODULE JS:

```javascript
import fs from "node:fs";

const someFunction = () => {};

export default someFunction;
```

Named Import:

```javascript
import {..., ....} from "..."
```

Named Export:

```javascript
export default {...., .....} // Used when multiple functions are defined in single file.
```

Note: Use a type: 'commonjs' or type: 'module' in package.json. commonjs type is default

---

DEFAULT IMPORT/EXPORT:

Import:

```javascript
import sum from "./mathUtils"; // 'sum' is an alias for the default 'add' function
```

Export:

```javascript
export default function add(a, b) {
  return a + b;
}
```

NAMED IMPORT/EXPORT:

Import:

```javascript
import { subtract, multiply as times } from "./mathUtils";

// 'subtract' is used as-is
// 'multiply' is aliased locally as 'times'

// Usage
console.log(sum(5, 3)); // 8
console.log(subtract(5, 3)); // 2
console.log(times(5, 3)); // 15
```

Export:

```javascript
export function subtract(a, b) {
  return a - b;
}

export function multiply(a, b) {
  return a * b;
}
```

---

NAMED ALIAS:

```javascript
import { TextInput as CDSTextInput } from "@carbon/react";
```

---

RELATIVE PATH (from reference of the current file) and ABSOLUTE PATH (from root level)

---
