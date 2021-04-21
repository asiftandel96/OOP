"""Implementation Inheritance vs Interface Inheritance
When you derive one class from another, the derived class inherits both:

The base class interface: The derived class inherits all the methods, properties, and attributes of the base class.

The base class implementation: The derived class inherits the code that implements the class interface.

Most of the time, you’ll want to inherit the implementation of a class, but you will want to implement multiple interfaces, so your objects can be used in different situations.

Modern programming languages are designed with this basic concept in mind. They allow you to inherit from a single class, but you can implement multiple interfaces.

In Python, you don’t have to explicitly declare an interface. Any object that implements the desired interface can be used in place of another object. This is known as duck typing. Duck typing is usually explained as “if it behaves like a duck, then it’s a duck.”

To illustrate this, you will now add a DisgruntledEmployee class to the example above which doesn’t derive from Employee:
"""


class disgruntledEmployee():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 10000000


"""The DisgruntledEmployee class doesn’t derive from Employee, but it exposes the same interface required by the PayrollSystem. The PayrollSystem.calculate_payroll() requires a list of objects that implement the following interface:

An id property or attribute that returns the employee’s id
A name property or attribute that represents the employee’s name
A .calculate_payroll() method that doesn’t take any parameters and returns the payroll amount to process
All these requirements are met by the DisgruntledEmployee class, so the PayrollSystem can still calculate its payroll.

As you can see, the PayrollSystem can still process the new object because it meets the desired interface.

Since you don’t have to derive from a specific class for your objects to be reusable by the program, you may be asking why you should use inheritance instead of just implementing the desired interface. The following rules may help you:

Use inheritance to reuse an implementation: Your derived classes should leverage most of their base class implementation. They must also model an is a relationship. A Customer class might also have an id and a name, but a Customer is not an Employee, so you should not use inheritance.

Implement an interface to be reused: When you want your class to be reused by a specific part of your application, you implement the required interface in your class, but you don’t need to provide a base class, or inherit from another class.
"""
