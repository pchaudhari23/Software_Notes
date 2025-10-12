https://playcode.io/ - Javascript playground

Instead of many if else: use
i.Ternary Operators
ii.Switch Statements
iii.Logical Operators (&& and ||)
iv.Lookup Maps

Lookup maps/lookup object: Eg:
function checkBestStudent(subject) {
var bestStudent = "";
var lookup = {
"maths": "Adams Milner",
"english": "Akande Olalekan Toheeb",
"chemistry": "Chicago",
"physics": "Denver",
"biology": "Easy"
};
bestStudent = lookup[subject];
console.log(bestStudent);
}

checkBestStudent("maths");

---

- Implement a loop counter to avoid getting stuck into infinite loop. On exceeding a count number, take an action to break and come out of loop.
- Store all the strings in a constants file and use constants wherever required.

---

Use spread operator to copy an object or to duplicate it and manipulate it.

var obj1 = {'key1':'val1', 'key2':'val2'}
var obj2 = {...obj1}
obj2 //{key1: 'val1', key2: 'val2'}

---

Javascript object keys could be in quotes or without quotes.
{
"PageSize": pageSize,
"PageCount": pageCount
}
OR
{
PageSize: pageSize,
PageCount: pageCount
}
if key and value both are same, then shorthand expression - use only one word for both.
{
pageSize: pageSize,
}
could be
{
pageSize
}

---

ARRAY INTERSECTION: let intersection = arr1.filter(x => arr2.includes(x));
ARRAY DIFFERENCE: let difference = arr1.filter(x => !arr2.includes(x));

---

- The this keyword is used to get/access or to set/modify/assign a value to the data member variable of a class, in that class itself.
- The scope of this keyword to be used on a data memberis in that particular class.
- this keyword is used on the data member of a class and not on the member function.

Eg:
class Customer{
int customerID;

    void setCustomerID(int ID){
    	this.customerID = ID;
    }

}

---

JSON:
JSON.stringify(Javascript Object) - Convert a JS Object to string
JSON.parse(JSON String) - Convert a JSON String to JS Object
toString(), parseInt(), parseFloat()

---

HTML String:

HTML Document:

1. HTML DOM -> HTML String
2. HTML String -> HTML DOM
   const parser = new DOMParser();
   var HTMLDocumentDOM = parser.parseFromString(htmlString, "text/html");

To make base64 of an HTML file:
1.Get the string representation of that html file - using DOMParser (its used to create a DOM from any string)
2.Covert that string to base64 - using btoa()

---

BASE 64:

- Encoded format of PDF, image, HTML page etc in the form of long string of characters.
- Binary string: A representation of a file format (Eg: HTML, PDF, Image etc.) as a string of binary numbers.
- Any media type with any extension can be converted to base64 and vice versa.
- File <-> Binary string <-> Base64 <-> File

btoa() - Binary string to Base 64
atob() - Base 64 to Binary string

BLOB file type??

base64 to blob - new Blob()
base64 to file - new File()

---

Type check: ===
Null check: ?. - checks that something should not be null or undefined. used to fix error - cannot read property of undefined or use an empty array with OR condition (SomedatainArray || [])

- ...args - array of aruguments - rest operator - when it's not known beforehand how many props would be there. In react it's ...props - object of props when number of props is not known

---

Query parameters:

- Occurs in the url after the domain name. Starts with a ? and seperated key value pairs by &
  Eg: localhost:3000?name=John&surname=Watson&age=25
  query parameters - started in the url after ? and parameters are seperated by &
  query parameters in above example are, name, surname and age

Path parameters:

- Occurs in the url path. Mentioned in curly braces in url path
- Eg: getdata/{product}/{id}

URL string functions:

1. window.location.href - gives URL
2. window.location.pathname - path of URL
3. window.location.search - query string parameters

---

Modelling - we need to define datatype explicitly in typescript. Javascript infers datatype automatically.

- Create objects using Model class in models folder
- Create datatypes using interfaces in types folder
  Creating type interfaces will give type safety.
  Type safety means the is no need to use generics datatype like Object or any or base datatype` but specific datatype eg: Customer object

---

TIPS & TRICKS:
