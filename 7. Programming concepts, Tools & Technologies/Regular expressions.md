- A regular expression, regex or regexp is a sequence of characters that define a search pattern.
- A regular expression is always within single quotes or between /..../ ???
  https://regex101.com/

---

Regex Quantifiers : The quantifiers specify the number of occurrences of a character.

1. \*: 0 or more occurances
2. +: 1 or more occurances
3. ? : 0 or 1 occurances
4. X{n} : X occurs n times only
5. X{n,} : X occurs n or more times
6. X{y,z} : X occurs at least y times but less than z times
7. '[a-zA-Z]' : any alphabet (lower or uppercase)
8. '[a-zA-Z0-9]' : any alphabet or number (alphanumeric character)
9. . : any character
10. ^ : starting position
11. $ : end position
12. [abcde..] : any character between bracket (a or b or c or d or e)

---

Regex Character classes :

1. [abc] : a, b, or c (simple class)
2. [^abc] : Any character except a, b, or c (negation)
3. [a-zA-Z] : a through z or A through Z, inclusive (range)
4. [a-d[m-p]] : a through d, or m through p: [a-dm-p] (union)
5. [a-z&&[def]] : d, e, or f (intersection)
6. [a-z&&[^bc]] : a through z, except for b and c: [ad-z] (subtraction)
7. [a-z&&[^m-p]] : a through z, and not m through p: [a-lq-z](subtraction)

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
   4.^[^Ss] - starting with anything except S or s i.e not starting with S or s.
4. name starting with k: 'k%' or /^k/
5. name ending with k: '%k' or /k$/
6. name with k in between: '%k%'
7. starting with A, ending with S, R at 3rd position: 'A_R%S'
8. Name containing 5 characters ending with T: '----T'
9. Words having Amitabh or amitabh: /^[Aa]mitabh/

---
