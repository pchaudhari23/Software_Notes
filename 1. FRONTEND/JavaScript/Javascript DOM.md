Inside head tag of HTML:
Import CSS - <link rel="stylesheet" href="report.css" />
Import JS - <script src="./report.js"></script>

All operations done on document object - document.querySelector() etc
Document is complete HTML of that web page

- HTML DOM Node
- element: It could be document or any DOM node

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

- document.querySelector("") => [] for data attributes, . for class and # for id attributes

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

1. element.addEventListner(event, callback function) - Eg: element.addEventListner("click", (event) => {})
2. element.removeEventListner(event, callback function)
3. Event bubbling/ capturing:
   element.addEventListner(event, callback function) -
   Eg: element.addEventListner("click", (event) => {
   console.log('Event occured'),
   }, { capture:true })

4. Stop event propogation:
   element.addEventListner(event, callback function) -
   Eg: element.addEventListner("click", (event) => {
   console.log('Event occured'),
   event.stopPropogation
   })

5. Run event only once:
   element.addEventListner(event, callback function) -
   Eg: element.addEventListner("click", (event) => {
   console.log('Event occured'),
   }, { once:true })

6. Event Delegation:
   element.addEventListner("click", (event) => {
   if(event.target.matches('div')) {
   console.log('hi')
   }
   })

---
