"""What are Inheritance and Composition:-

Inheritance and composition are two major concepts in object oriented programming that model the relationship between two classes. They drive the design of an application and determine how the application should evolve as new features are added or requirements change.
Both of them enable code reuse, but they do it in different ways.

What’s Inheritance?
Inheritance models what is called an is a relationship. This means that when you have a Derived class that inherits from a Base class, you created a relationship where Derived is a specialized version of Base.

Inheritance is represented using the Unified Modeling Language


Note: In an inheritance relationship:

1. Classes that inherit from another are called derived classes, subclasses, or subtypes.

2. Classes from which other classes are derived are called base classes or super classes.

3. A derived class is said to derive, inherit, or extend a base class.


Let’s say you have a base class Animal and you derive from it to create a Horse class. The inheritance relationship states that a Horse is an Animal. This means that Horse inherits the interface and implementation of Animal, and Horse objects can be used to replace Animal objects in the application.

This is known as the Liskov substitution principle. The principle states that “in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program”.

You’ll see in this article why you should always follow the Liskov substitution principle when creating your class hierarchies, and the problems you’ll run into if you don’t.

What’s Composition?

Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.

Composition is represented through a line with a diamond at the composite class pointing to the component class. The composite side can express the cardinality of the relationship. The cardinality indicates the number or valid range of Component instances the Composite class will contain.

In the diagram above, the 1 represents that the Composite class contains one object of type Component. Cardinality can be expressed in the following ways:

A number indicates the number of Component instances that are contained in the Composite.
The * symbol indicates that the Composite class can contain a variable number of Component instances.
A range 1..4 indicates that the Composite class can contain a range of Component instances. The range is indicated with the minimum and maximum number of instances, or minimum and many instances like in 1..*.
Note: Classes that contain objects of other classes are usually referred to as composites, where classes that are used to create more complex types are referred to as components.

For example, your Horse class can be composed by another object of type Tail. Composition allows you to express that relationship by saying a Horse has a Tail.

Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes. Both Horse and Dog classes can leverage the functionality of Tail through composition without deriving one class from the other.

#An Overview of Inheritance in Python:-

Everything in Python is an object. Modules are objects, class definitions and functions are objects, and of course, objects created from classes are objects too.

Inheritance is a required feature of every object oriented programming language. This means that Python supports inheritance, and as you’ll see later, it’s one of the few languages that supports multiple inheritance.

When you write Python code using classes, you are using inheritance even if you don’t know you’re using it. Let’s take a look at what that means.

"""

#Object Super Class

class MyClass:
        pass

'''You declared a class MyClass that doesn’t do much, but it will illustrate the most basic inheritance concepts. Now that you have the class declared, you can use the dir() function to list its members:'''

c=MyClass()
print()
print(dir(c))


"""dir() returns a list of all the members in the 
specified object. You have not declared any members in MyClass"""


#Exceptions Are an Exception
'''
Every class that you create in Python will implicitly derive from object. The exception to this rule are classes used to indicate errors by raising an exception.
class MyError:
        pass

raise MyError()

You created a new class to indicate a type of error. Then you tried to use it to raise an exception. An exception is raised but the output states that the exception is of type TypeError not MyError and that all exceptions must derive from BaseException.

BaseException is a base class provided for all error types. To create a new error type, you must derive your class from BaseException or one of its derived classes. The convention in Python is to derive your custom error types from Exception, which in turn derives from BaseException.

'''

"""
class MyError(Exception):
       pass

raise MyError()

"""

#'''As you can see, when you raise MyError, the output correctly states the type of error raised.'''

"""Creating Class Hierarchies
Inheritance is the mechanism you’ll use to create hierarchies of related classes. These related classes will share a common interface that will be defined in the base classes. Derived classes can specialize the interface by providing a particular implementation where applies.

In this section, you’ll start modeling an HR system. The example will demonstrate the use of inheritance and how derived classes can provide a concrete implementation of the base class interface.

The HR system needs to process payroll for the company’s employees, but there are different types of employees depending on how their payroll is calculated.

You start by implementing a PayrollSystem class that processes payroll:"""





