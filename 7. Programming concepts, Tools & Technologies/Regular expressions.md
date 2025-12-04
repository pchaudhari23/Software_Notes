- A regular expression, regex or regexp is a sequence of characters that define a search pattern.
- A regular expression is always between forward slashes - /..../
- https://regex101.com/

---

Regex Quantifiers : The quantifiers specify the number of occurrences of a character.

1. ^ : start of string
2. $ : end of string
3. \*: 0 or more occurances
4. +: 1 or more occurances
5. ? : 0 or 1 occurances
6. X{n} : X occurs n times only
7. X{n,} : X occurs n or more times
8. X{y,z} : X occurs between y and z
9. '[a-zA-Z]' : any alphabet (lower or uppercase)
10. '[a-zA-Z0-9]' : any alphabet or number (alphanumeric character)
11. . : any character
12. [abcde..] : any character between bracket (a or b or c or d or e)

---

Regex Character classes :

1. [abc] : a, b, or c (simple class)
2. [^abc] : Any character except a, b, or c (negation)
3. [a-zA-Z] : a through z or A through Z, inclusive (range)
4. [a-dm-p] : a through d, or m through p (union)

---

Regex Metacharacters : The regular expression metacharacters work as shortcodes.

1. . : Any character (may or may not match terminator)
2. \d : Any digits, short of [0-9]
3. \D : Any non-digit, short for [^0-9]
4. \s : Any whitespace character, short for [\t\n\x0B\f\r]
5. \S : Any non-whitespace character, short for [^\s]
6. \w : Any word character, short for [a-zA-Z_0-9]
7. \W : Any non-word character, short for [^\w]
8. \b : A word boundary
9. \B : A non word boundary

---

EXAMPLES:

1. Words starting with Wil : /^Wil/
2. Words ending with ces: /ces$/
3. Words with reg somewhere in between: /._reg._/
4. ^[^Ss] - starting with anything except S or s i.e not starting with S or s.
5. name starting with k: /^k/
6. name ending with k: /k$/
7. name with k in between: /k/
8. starting with A, ending with S, R at 3rd position: /^A.R.\*S$/
9. Name containing 5 characters ending with T: '----T'
10. Words having Amitabh or amitabh: /^[Aa]mitabh/

---
