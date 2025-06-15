GENERAL FUNCTIONS:

---

DOM Traversal, Manipulation & Event Handling:

---

CHECKBOXES:
$(...).is(':checked')
$(...).filter(':checked').length > 0
$(...:checked).length > 0

---

CHECKLIST:

---

RADIO BUTTON:

---

INPUT:

---

DROPDOWN - SINGLE SELECT:
$(...).currentValue("..") - SHB Only

---

DROPDOWN - MULTI SELECT:
$(...).selectedValues("..") - SHB Only

---

COMBOBOX

---

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

```

```
