Inside head tag of HTML:

```JavaScript
<link rel="stylesheet" href="report.css" /> // Import CSS
<script src="./report.js"></script> // Import JS
```

---

DOM TRAVERSAL:

1. document.getElementById('medications')
2. document.querySelector("[data-type='generalInfo']")
3. document.querySelector("#grandparent-id") => to get element by id
4. document.querySelector(".grandparent") => to get element by class
5. document.querySelector("[data-type='generalInfo']")
6. document.querySelectorAll("[data-type='generalInfo']")
7. Array.from(document.querySelectorAll("[data-type='generalInfo']")) - to get output in Array form
8. document.getElementsByTagName()
9. element.children - to get children, use Array.from() for array output
10. element.parentElement
11. element.closest('.grandparent')
12. element.nextElementSibling
13. element.previousElementSibling
14. const listItem = document.querySelector("li:last-child") - get last child, first child etc
15. document.querySelector("") => [] for data attributes, . for class and # for id attributes

---

DOM MANIPULATION:

1. document.append()
2. document.remove()
3. document.appendChild()
4. document.removeChild()
5. document.createElement()
6. div.innerText = ''
7. div.textContent = ''
8. div.innerHTML = ''
9. div.getAttribute(), div.hasAttribute()
10. div.setAttribute()
11. div.removeAttribute()
12. element.classList
13. element.classList.add()
14. element.classList.remove()
15. element.classList.toggle()
16. element.style.display = none OR element.style.display = block
17. element.style.backgroundColor = 'red'

Custom data attributes: 19. data-.... 20. div.dataset. 21. access table rows in table using js - .rows 22. access tr in td using js - .cells 22. document.getElementById("AddPatientExpand").click() - to automatically click the button

---

EVENT HANDLING:

1. element.addEventListener(event, callback function) - Eg: element.addEventListener("click", (event) => {})
2. element.removeEventListner(event, callback function)
3. Event bubbling/ capturing:
   element.addEventListener(event, callback function) -
   Eg: element.addEventListener("click", (event) => {
   console.log('Event occured'),
   }, { capture:true })
4. Stop event propogation:
   element.addEventListener(event, callback function) -
   Eg: element.addEventListener("click", (event) => {
   console.log('Event occured'),
   event.stopPropogation
   })
5. Run event only once:
   element.addEventListener(event, callback function) -
   Eg: element.addEventListener("click", (event) => {
   console.log('Event occured'),
   }, { once:true })
6. Event Delegation:
   element.addEventListener("click", (event) => {
   if(event.target.matches('div')) {
   console.log('hi')
   }
   })
7. addEventListener
8. event.target.name
9. event.target.value
10. event.preventDefault
11. event.stopPropogation

---

jQuery:

$(...).find() - No need to write $($(.....)) - It returns all the elements
$(...).get()
$(...).css()
$(...).val()
$(...).parent()
$(...).children()
$(...).next()
$(...).prev()
$(...).hasClass()
$(...).closest()
$(...).each()
$(...).prop()
$(...).on()
$(...).data()
$(...).closest() - use to find nearest ancestor with given selector query - useful instead of using $(...).parent().parent().parent().parent().parent()....
$(...).closest(".myClass"); // by class
$(...).closest('[href="#foo"]'); OR $(...).closest("li:has(\*[data-findme])") // by attribute

---

Miscelleneous:

JSON:

- JSON.stringify(Javascript Object) - Convert a JS Object to string
- JSON.parse(JSON String) - Convert a JSON String to JS Object
- parseInt(): string => integer
- parseFloat(): string => float,
- toString(): data => string

HTML Document:

1. HTML DOM => HTML String
2. HTML String => HTML DOM
   const parser = new DOMParser();
   var HTMLDocumentDOM = parser.parseFromString(htmlString, "text/html");

To make base64 of an HTML file:

1. Get the string representation of that html file - using DOMParser (its used to create a DOM from any string)
2. Covert that string to base64 - using btoa()

BASE 64:

- Encoded format of PDF, image, HTML page etc in the form of long string of characters.
- Binary string: A representation of a file format (Eg: HTML, PDF, Image etc.) as a string of binary numbers.
- Any media type with any extension can be converted to base64 and vice versa.
- File <=> Binary string <=> Base64 <=> File
- btoa() - Binary string to Base 64
- atob() - Base 64 to Binary string
- BLOB file type??
- base64 to blob - new Blob()
- base64 to file - new File()

URL string functions:

1. window.location.href - gives URL
2. window.location.pathname - path of URL
3. window.location.search - query string parameters

---
