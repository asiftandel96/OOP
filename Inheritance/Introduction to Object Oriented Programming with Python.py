"""What is Object Oriented Programming
Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. In this tutorial, you’ll learn the basics of object-oriented programming in Python.
Conceptually, objects are like the components of a system. Think of a program as a factory assembly line of sorts. At each step of the assembly line a system component processes some material, ultimately transforming raw material into a finished product.
An object contains data, like the raw or preprocessed materials at each step on an assembly line, and behavior, like the action each assembly line component performs.

How to Define a Class:-
All class definitions start with the class keyword, which is followed by the name
of the class and a colon. Any code that is indented below the class definition is considered part of the class’s body.

"""


# Creating A Simple Class to test if it is working or not

class Dog:
    pass  # pass keyword is used in Python to check if the program is running fine or not


class Dogg:
    """Notice that the .__init__() method’s signature is indented four spaces. The body of the method is indented by eight spaces. This indentation is vitally important. It tells Python that the .__init__() method belongs to the Dog class.

In the body of .__init__(), there are two statements using the self variable:

1. self.name = name creates an attribute called name and assigns to it the value of the name parameter.
2. self.age = age creates an attribute called age and assigns to it the value of the age parameter.
Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance."""

    def __init__(self, name, age):
        self.name = name  # name and age are instance attributes of the class
        self.age = age


"""Class Attributes
On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
Class attributes are defined directly beneath the first line of the class name and are indented by four spaces. They must always be assigned an initial value. When an instance of the class is created, class attributes are automatically created and assigned to their initial values.

Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.
"""


class Dogg_attribute:
    color = 'Red'  # This is a class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


"""Instantiate an Object in Python"""
'''Creating a new object from a class is called instantiating an object. You can instantiate a new Dog object by 
typing the name of the class, followed by opening and closing parentheses: '''

print(Dog())

'''You now have a new Dog object at 0x000000. This funny-looking string of letters and numbers is a memory address 
that indicates where the Dog object is stored in your computer’s memory. Note that the address you see on your screen 
will be different. '''

# Now instantiate a second Dog object:
print()
print(Dog())

# To see this another way, type the following:

a = Dog()
b = Dog()
print()
print(a == b)

"""In this code, you create two new Dog objects and assign them to the variables a and b. When you compare a and b 
using the == operator, the result is False. Even though a and b are both instances of the Dog class, they represent 
two distinct objects in memory. """

# Class and Instance Attributes

"""Now create a new Dog class with a class attribute called .species and two instance attributes called .name and 
.age """


# This is A Instance Attributes Example
class Dog_classA:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


'''To instantiate objects of this Dog class, you need to provide values for the name and age. If you don’t, 
then Python raises a TypeError: '''

# b=Dog_classA()

'''To pass arguments to the name and age parameters, put values into the parentheses after the class name:'''

buddy = Dog_classA('Turfy', 9, 'Brown')
miles = Dog_classA('Adel', 10, 'Black')

'''This creates two new Dog instances—one for a nine-year-old dog named Buddy and one for a four-year-old dog named Miles.

The Dog class’s .__init__() method has three parameters, so why are only two arguments passed to it in the example?

When you instantiate a Dog object, Python creates a new instance and passes it to the first parameter of .__init__(). This essentially removes the self parameter, so you only need to worry about the name and age parameters.'''
print()
print('The name of the first dog is', buddy.name)
print('The name of the second dog is', miles.name)


# Class Attributes

class Car:
    brand = 'Mercedes'

    def __init__(self, windows, door, features, enginetype):
        self.windows = windows
        self.door = door
        self.features = features
        self.enginetype = enginetype

    def display(self):
        print('The window of the car is', self.windows)
        print('The door of the car is', self.door)
        print('The features of the car is', self.features)
        print('The enginetype of the car is', self.enginetype)

    def drivingexperience(self):
        print('The drivingexperience is good')


Audi_Brand = Car(4, 4, 'Good Miles and Other', 'Diesel')
print()
print(Audi_Brand.windows)
print(Audi_Brand.door)
Audi_Brand.brand = 'Audi'  # The key takeaway here is that custom objects are mutable by default. An object is mutable
# if it can be altered dynamically. For example, lists and dictionaries are mutable, but strings and tuples are
# immutable.
print(Audi_Brand.brand)
Audi_Brand.display()
Audi_Brand.drivingexperience()

# Instance Methods

'''Instance methods are functions that are defined inside a class and can only be called from an instance of that 
class. Just like .__init__(), an instance method’s first parameter is always self. '''


class Dog_Description:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Methods
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another Instance Method

    def speak(self, sound):
        return f"{self.name} says {sound}"


"""This Dog_Description class has two instance methods:

1. .description() returns a string displaying the name and age of the dog.
2. .speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.

In the above Dog class, .description() returns a string containing information about the Dog instance miles. 
When writing your own classes, it’s a good idea to have a method that returns a string containing useful information about an instance of the class. However, .description() isn’t the most Pythonic way of doing this.
"""

a = Dog_Description('Buddy', 9)
print()
print('-----INSTANCE METHODS----')
print(a.description())
print(a.speak('Woof Woof'))
print()
print('---a is the object of class Dog_description ')
print(a)  # a is the object of class Dog_Description

"""When you print(a), you get a cryptic looking message telling you that miles is a Dog object at the memory 
address 0x00aeff70. This message isn’t very helpful. You can change what gets printed by defining a special instance 
method called .__str__(). """


class Dog_dunder:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Dunder Methods"""
        return f"{self.name} is {self.age} years old"


print()
b = Dog_dunder('Buddy', 10)
print(b)

'''Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python. Although too advanced a topic for a beginning Python book, understanding dunder methods is an important part of mastering object-oriented programming in Python.'''



