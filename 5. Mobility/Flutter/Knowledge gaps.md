Clean architecture - Understanding gaps

1. What is the point of clean architecture? How is it better?
2. What should be the naming convention of files and the methods inside them?
3. OOPs basic required for this?
4. BloC connection in this

---

Inheritance:
extends

super constructor

Abstraction:
implements
@override - to method

required????
factory????

---

Code sequence:

1. Entity
2. domain repo
3. usecase
4. model
5. repo impl
6. data source

---

To return an Either from function:
return Right(...);
return Left(...);

---

call fold() on Either
