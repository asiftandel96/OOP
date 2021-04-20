"""Choosing Between Inheritance and Composition in Python So far, you’ve seen how inheritance and composition work in
Python. You’ve seen that derived classes inherit the interface and implementation of their base classes. You’ve also
seen that composition allows you to reuse the implementation of another class.

You’ve implemented two solutions to the same problem. The first solution used multiple inheritance, and the second
one used composition.

You’ve also seen that Python’s duck typing allows you to reuse objects with existing parts of a program by
implementing the desired interface. In Python, it isn’t necessary to derive from a base class for your classes to be
reused.

At this point, you might be asking when to use inheritance vs composition in Python. They both enable code reuse.
Inheritance and composition can tackle similar problems in your Python programs.

The general advice is to use the relationship that creates fewer dependencies between two classes. This relation is
composition. Still, there will be times where inheritance will make more sense.

The following sections provide some guidelines to help you make the right choice between inheritance and composition
in Python.

Inheritance to Model “Is A” Relationship Inheritance should only be used to model an is a relationship. Liskov’s
substitution principle says that an object of type Derived, which inherits from Base, can replace an object of type
Base without altering the desirable properties of a program.

Liskov’s substitution principle is the most important guideline to determine if inheritance is the appropriate design
solution. Still, the answer might not be straightforward in all situations. Fortunately, there is a simple test you
can use to determine if your design follows Liskov’s substitution principle.

Let’s say you have a class A that provides an implementation and interface you want to reuse in another class B. Your
initial thought is that you can derive B from A and inherit both the interface and implementation. To be sure this is
the right design, you follow theses steps:

Evaluate B is an A: Think about this relationship and justify it. Does it make sense?

Evaluate A is a B: Reverse the relationship and justify it. Does it also make sense?

If you can justify both relationships, then you should never inherit those classes from one another. Let’s look at a
more concrete example.

You have a class Rectangle which exposes an .area property. You need a class Square, which also has an .area. It
seems that a Square is a special type of Rectangle, so maybe you can derive from it and leverage both the interface
and implementation.

Before you jump into the implementation, you use Liskov’s substitution principle to evaluate the relationship.

A Square is a Rectangle because its area is calculated from the product of its height times its length. The constraint is that Square.height and Square.length must be equal.

It makes sense. You can justify the relationship and explain why a Square is a Rectangle. Let’s reverse the relationship to see if it makes sense.

A Rectangle is a Square because its area is calculated from the product of its height times its length. The difference is that Rectangle.height and Rectangle.width can change independently.

It also makes sense. You can justify the relationship and describe the special constraints for each class. This is a good sign that these two classes should never derive from each other.

You might have seen other examples that derive Square from Rectangle to explain inheritance. You might be skeptical with the little test you just did. Fair enough. Let’s write a program that illustrates the problem with deriving Square from Rectangle.

First, you implement Rectangle. You’re even going to encapsulate the attributes to ensure that all the constraints are met:
"""


class Rectangle:

    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height


"""The Rectangle class is initialized with a length and a height, and it provides an .area property that returns the area. The length and height are encapsulated to avoid changing them directly.

Now, you derive Square from Rectangle and override the necessary interface to meet the constraints of a Square:"""


class Square(Rectangle):

    def __init__(self, side_size):
        super().__init__(side_size, side_size)


"""The Square class is initialized with a side_size, which is used to initialize both components of the base class. 
Now, you write a small program to test the behavior: """
print('---NORMAL')
rectangle = Rectangle(2, 4)

assert rectangle.area == 8

square = Square(2)

assert square.area == 4

print('OK!')

"""The program executes correctly, so it seems that Square is just a special case of a Rectangle.

Later on, you need to support resizing Rectangle objects, so you make the appropriate changes to the class:"""
print()
print('---AFTER RESIZE METHOD IMPLEMENTATION')
rectangle.resize(3, 5)

assert rectangle.area == 15

print('OK!')

"""The assertion passes, and you see that the program runs correctly.

So, what happens if you resize a square? Modify the program, and try to modify the square object:"""
print()
print('AFTER SQUARE RESIZE')

square.resize(3, 5)

print(f'Square area:{square.area}')


"""The program shows that the new area is 15 like the rectangle object. The problem now is that the square object no 
longer meets the Square class constraint that the length and height must be equal. 

How can you fix that problem? You can try several approaches, but all of them will be awkward. You can override 
.resize() in square and ignore the height parameter, but that will be confusing for people looking at other parts of 
the program where rectangles are being resized and some of them are not getting the expected areas because they are 
really squares. 

In a small program like this one, it might be easy to spot the causes of the weird behavior, but in a more complex 
program, the problem will be harder to find. 

The reality is that if you’re able to justify an inheritance relationship between two classes both ways, you should 
not derive one class from another. 

In the example, it doesn’t make sense that Square inherits the interface and implementation of .resize() from Rectangle. That doesn’t mean that Square objects can’t be resized. It means that the interface is different because it only needs a side_size parameter.

This difference in interface justifies not deriving Square from Rectangle like the test above advised.

"""