# Python Notes

> A beginner's reference guide to Python fundamentals

---

## Table of Contents

1. [Running Python](https://claude.ai/new?incognito=#1-running-python)
2. [Key Features](https://claude.ai/new?incognito=#2-key-features)
3. [Data Types](https://claude.ai/new?incognito=#3-data-types)
4. [Built-in Functions](https://claude.ai/new?incognito=#4-built-in-functions)
5. [Dates](https://claude.ai/new?incognito=#5-dates)
6. [Command Line Arguments](https://claude.ai/new?incognito=#6-command-line-arguments)
7. [Conditionals (if/elif/else)](https://claude.ai/new?incognito=#7-conditionals-ifelifelse)
8. [Logical Operators](https://claude.ai/new?incognito=#8-logical-operators)
9. [Arithmetic &amp; Assignment Operators](https://claude.ai/new?incognito=#9-arithmetic--assignment-operators)
10. [Lists](https://claude.ai/new?incognito=#10-lists)
11. [Loops](https://claude.ai/new?incognito=#11-loops)
12. [Dictionaries](https://claude.ai/new?incognito=#12-dictionaries)
13. [Functions](https://claude.ai/new?incognito=#13-functions)
14. [Error Handling](https://claude.ai/new?incognito=#14-error-handling)
15. [Collections: Tuples &amp; Sets](https://claude.ai/new?incognito=#15-collections-tuples--sets)
16. [Libraries](https://claude.ai/new?incognito=#16-libraries)
17. [Coming Up Next](https://claude.ai/new?incognito=#17-coming-up-next)

---

## 1. Running Python

```bash
# Start Python REPL (interactive shell)
python

# Run a specific file
python filename.py

# Check versions
py -3 --version
pip3 --version
```

**In VS Code:**

* `Ctrl + `` → Open existing/closed terminal
* `Ctrl + Shift + `` → Open a new terminal

**Ways to run Python:**

* `python` in Command Prompt / Terminal
* IDLE (comes pre-installed with Python)
* VS Code terminal → `python filename.py`
* REPL — interactive shell, no file needed

---

## 2. Key Features

| Feature                     | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| **Interpreted**       | Executed line by line                                     |
| **Object-Oriented**   | Supports classes and objects                              |
| **Dynamically Typed** | No need to declare types (`var`,`int`,`bool`, etc.) |
| **REPL**              | Read-Eval-Print-Loop — run code interactively in the CLI |

---

## 3. Data Types

| Category           | Types                                |
| ------------------ | ------------------------------------ |
| **Numeric**  | `int`,`float`                    |
| **Sequence** | `str`,`list`,`tuple`,`range` |
| **Mapping**  | `dict`                             |
| **Set**      | `set`,`frozenset`                |
| **Boolean**  | `bool`                             |
| **None**     | `None`(equivalent to null)         |

---

## 4. Built-in Functions

| Function             | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `print(x)`         | Print to the console                                    |
| `input('message')` | Capture user input (always returns a `str`)           |
| `type(x)`          | Check the data type of a variable                       |
| `int(x)`           | Convert string/float to integer                         |
| `float(x)`         | Convert string/int to float                             |
| `str(x)`           | Convert integer or float to string                      |
| `round(x)`         | Round to the nearest whole number                       |
| `abs(x)`           | Return absolute value (removes negative sign)           |
| `len(x)`           | Return the length of a string, list, etc.               |
| `min(list)`        | Return the smallest value in a list                     |
| `max(list)`        | Return the largest value in a list                      |
| `any([])`          | Returns `True`if any item in the iterable is `True` |
| `lower()`          | Convert a string to lowercase                           |

**Rounding rules for `round()`:**

* Decimal > 0.5 → rounds **up**
* Decimal < 0.5 → rounds **down**
* Decimal = 0.5 → rounds to nearest **even** integer

**Math library:**

```python
from math import ceil, floor
```

---

## 5. Dates

```python
from datetime import date

print(date.today())   # e.g. 2026-06-12
```

---

## 6. Command Line Arguments

Arguments passed in the CLI before running a file.

```bash
python program.py 12 87
```

```python
import sys

print(sys.argv)      # ['program.py', '12', '87']
print(sys.argv[0])   # program.py  (the file name)
print(sys.argv[1])   # 12          (first argument)
```

---

## 7. Conditionals (if/elif/else)

> ⚠️ Indentation is **mandatory** in Python.

```python
if test_expression:
    # runs if condition is True
elif test_expression:
    # runs if previous condition was False and this is True
elif test_expression:
    # another optional check
else:
    # runs if none of the above were True
```

**Example:**

```python
object_size = 10

if object_size > 10:
    print("Large object!")
elif object_size > 5:
    print("Medium object.")
else:
    print("Small object.")
```

---

## 8. Logical Operators

```python
# AND — both conditions must be True
if size > 5 and proximity < 1000:
    print("Evasive maneuvers required")

# OR — at least one condition must be True
if size > 5 or proximity < 500:
    print("Stay alert")
```

---

## 9. Arithmetic & Assignment Operators

**Arithmetic:**

| Operator | Description                     | Example         |
| -------- | ------------------------------- | --------------- |
| `+`    | Addition                        | `5 + 3 = 8`   |
| `-`    | Subtraction                     | `5 - 3 = 2`   |
| `*`    | Multiplication                  | `5 * 3 = 15`  |
| `/`    | Division                        | `7 / 2 = 3.5` |
| `//`   | Floor division (integer result) | `7 // 2 = 3`  |
| `%`    | Modulo (remainder)              | `7 % 2 = 1`   |

**Assignment:**

| Operator   | Equivalent    |
| ---------- | ------------- |
| `x = 5`  | assign        |
| `x += 2` | `x = x + 2` |
| `x -= 2` | `x = x - 2` |
| `x *= 2` | `x = x * 2` |
| `x /= 2` | `x = x / 2` |

**Order of Operations (PEMDAS):**

1. Parentheses
2. Exponents
3. Multiplication & Division
4. Addition & Subtraction

---

## 10. Lists

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

**Common operations:**

```python
len(planets)              # Length of list → 8
planets.append("Pluto")   # Add item to end
planets.pop()             # Remove last item
planets.index("Jupiter")  # Find index of an item
planets[-1]               # Negative index → last item ("Neptune")
```

**Min / Max:**

```python
gravity = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
min(gravity)   # → 0.377
max(gravity)   # → 2.36
```

**Slicing:**

```python
planets[0:2]    # ['Mercury', 'Venus']
planets[2:]     # From index 2 to end
planets[:3]     # From start to index 2
```

**Sorting:**

```python
planets.sort()                 # Alphabetical (ascending)
planets.sort(reverse=True)     # Reverse order
```

**Joining two lists:**

```python
group_a = ["Metis", "Adrastea", "Amalthea", "Thebe"]
group_b = ["Io", "Europa", "Ganymede", "Callisto"]
all_moons = group_a + group_b
```

---

## 11. Loops

### while loop

Use when the number of repetitions is  **unknown** .

```python
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a planet, or 'done' to stop: ")
```

### for loop

Use to iterate over a sequence.

```python
countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)

print("Blast off!! 🚀")
```

**Destructuring in a for loop:**

```python
for left, right in pairs_list:
    print(left, right)
```

---

## 12. Dictionaries

```python
planet = {
    'name': 'Earth',
    'moons': 1
}
```

**CRUD Operations:**

```python
# Read
print(planet.get('name'))   # Safe — returns None if key missing
print(planet['name'])       # Direct — raises error if key missing

# Update
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# Add a new key
planet['orbital period'] = 4333

# Remove a key
planet.pop('orbital period')
```

**Nested dictionary:**

```python
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# Access nested value
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
```

> ⚠️ Keys are  **case-sensitive** . `'Name'` ≠ `'name'`

**Iterating over a dictionary:**

```python
rainfall = {'october': 3.5, 'november': 4.2, 'december': 2.1}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
```

**Check if a key exists:**

```python
if 'december' in rainfall:
    rainfall['december'] += 1
else:
    rainfall['december'] = 1
```

**Sum all values:**

```python
total = 0
for value in rainfall.values():
    total += value

print(f'Total rainfall: {total}cm')
```

---

## 13. Functions

```python
# Basic function with return value
def rocket_parts():
    return "payload, propellant, structure"

# Function with fixed arguments
def generate_report(main_tank, external_tank, hydrogen_tank):
    print(f"Main: {main_tank}, External: {external_tank}, Hydrogen: {hydrogen_tank}")

generate_report(80, 70, 75)
```

**Keyword arguments (optional, with defaults):**

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi there")    # Hi there, Bob!
```

> ⚠️ Mandatory arguments must come **before** keyword arguments.

**Variable positional arguments (`*args`):**

```python
def variable_length(*args):
    print(args)   # args is a tuple

variable_length(1, 2, 3)
```

**Variable keyword arguments (`**kwargs`):**

```python
def fuel_report(**kwargs):
    for name, value in kwargs.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)
```

> 💡 If a function has no `return` statement, it implicitly returns `None`.

---

## 14. Error Handling

**Basic try/except:**

```python
try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")
```

**Capture the exception object:**

```python
try:
    open('config.txt')
except FileNotFoundError as err:
    print(f"Error: {err}")
```

**Handle multiple exceptions:**

```python
except (ValueError, TypeError):
    print("Value or Type error occurred")
```

**Raise an exception manually:**

```python
def str_to_bool(value):
    if value.lower() in ['yes', 'y']:
        return True
    elif value.lower() in ['no', 'n']:
        return False
    else:
        raise ValueError('Invalid entry — use yes/no/y/n')
```

**Parsing example (skip bad lines):**

```python
config = "fuel=4\noxygen=3\n$ invalid line"

parsed = {}
for line in config.split('\n'):
    try:
        key, value = line.split('=')
        parsed[key] = value
    except ValueError:
        print(f'Skipping unparseable line: {line}')
```

---

## 15. Collections: Tuples & Sets

### Tuple

* Ordered, **immutable** (cannot be changed after creation)
* Defined with `()`

```python
coordinates = (10.5, 20.3)
```

### Set

* Unordered, **no duplicates**
* Defined with `{}`

```python
unique_planets = {"Earth", "Mars", "Earth"}   # → {"Earth", "Mars"}
```

---

## 16. Libraries

| Library      | Use Case                       |
| ------------ | ------------------------------ |
| `numpy`    | Numerical computing, arrays    |
| `pandas`   | Data analysis and manipulation |
| `django`   | Full-featured web framework    |
| `flask`    | Lightweight web framework      |
| `nltk`     | Natural language processing    |
| `requests` | HTTP requests / calling APIs   |

---

## 17. Coming Up Next

* **Variable Scope** — local vs. global variables inside functions
* **Classes & Objects** — the foundation of object-oriented programming in Python
