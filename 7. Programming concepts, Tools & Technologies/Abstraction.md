ABSTRACT CLASSSES & INTERFACES:

1. Abstract class in JAVA:

- They are used to implement abtraction.
- Abstract classes cannot be instantiated i.e objects of abstract class cannot be created.
- It may or may not contain abstract methods thus providing partial abstraction (0 to 100%).
- Instance of an abstract class cannot be created, we can have references of abstract class type though.
- An abstract class can contain constructor in JAVA and a constructor of abstract class is called when an instance of a inherited cass is created.
- In JAVA, we can have an abstract class without any abstract method. This allows us to create classes that cannot be instantiated, but can only be inherited.
- Abstract classes can also have final methods (methods that cannot be overridden).
- Abstract method is a method which has only declaration and not implementation.
- A non abstract method or concrete method has declaration as well as implementation.

Example:
abstract class Car
{
abstract void engine(); //abstract method
void gearbox()
{
System.out.println("Automatic gear shift.");
}
}

class Audi extends Car //child class derived from the abstract class
{
void engine()
{
System.out.println("Powerful V12 Engine"); //abstract method's implementation given in child class
}
}

class Main
{
public static void main(String args[])
{
Car Q7 = new Audi(); /_constructor of child class is called to create an object of class Audi, since abstract class cannot be instantiated _/
Q7.engine(); //call the derived class method
}
}

---

2. Interfaces in JAVA:

- They are used to implement abstraction and achieve multiple inheritance.
- They provide complete (100%) abstraction by declaring all methods as abstract.
- Using interface, multiple inheritance can be achieved because the problem of ambiguity is solved as all the methods are abstract i.e implementation is not declared in the interface, but it is declared in the class which implements the interfaces.
- A class can extend only one class, but can implement one or more than one interfaces.
- An interface can extend one or more than one interface.

Example:
//interface declaration by first user
interface Drawable
{
void draw();
}

//interface implementation by second user
class Rectangle implements Drawable
{
public void draw()
{
System.out.println("Drawing a rectangle.");
}
}

class Circle implements Drawable
{
public void draw()
{
System.out.println("Drawing a circle.");
}
}

//interface used by third user
class Main
{
public static void main(String args[])
{
Drawable D = new Circle(); //Creates a circle object which implements Drawable interface
D.draw(); // prints "Drawing a circle."
}
}

---

3. Abstract class in C#:

- The abstract keyword is used to create abstract class.
- An abstract class is incomplete and hence cannot be instantiated.
- An abstract class can only be used as a base class.
- An abstract class cannot be sealed.
- An abstract class may contain abstarct memebers (methods, properties, indexers, events) but not mandatory.
- A non abstract class derived from an abstract class must provide implementations for all inherited abstract members.
- If a class inherits an abstract class, there are 2 options available for that class:
  Option 1:
  Provide implementation for all the abstract members inherited from base abstract class.
  Option 2:
  If the class does not wish to provide implementation for all the abstract members, inherited from the abstract class, then the class has to be marked as abstract.

Example:
public abstract class Car
{
public void engine(); //abstract method
}

public class Audi:Car
{
public override void engine()
{
Console.WriteLine("Powerful V12 engine.");
}

    public static void Main(string args[])
    {
    	Car Q7 = new Audi();
    	Q7.engine();
    }

}

---

4. Interface in C#:

- We create interfaces using interface keyword. Like classes, interfaces also contain properties, methods, delegates or events, but only declaration, no implementation.
- It is a compile time error to provide implementation for any interface member.
- Interface members are public by default and they don't allow explicit access modifiers.
- Interface cannot contain fields.
- If a class or a struct inherits from an interface, it must provide implementation for all interface members. Otherwise we get a compile time error.
- A class or a struct can inherit from more than one interface at the same time but where as a class cannot inherit from more than one class at the same time.
- Interfaces can inherit from other interfaces. A class that inherits this interface must provide implementation for all interface members in the entire interface inheritance chain.
- We cannot create an instance of an interface, but an interface reference variable can point to a derived class object.
- Interface naming convention: Interface names are prefixed with a capital I.

Example:
using System;

interface IDrawable
{
void draw(); //abstract method
}

interface IArea
{
void CalculateArea(); //another abstract method
}

public class Circle: IDrawable,IArea
{
public void draw()
{
Console.WriteLine("Drawing a circle");
}

    public void CalculateArea()
    {
    	Console.WriteLine("Calculating the circle area.");
    }

}

public class Program:Circle
{
public static void Main(string args[])
{
Cicle C1 = new Circle();
C1.draw(); // will print "Drawing a circle."
}
}

---
