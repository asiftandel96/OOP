"""
Description of the Topic

What is Polymorphism :

The word polymorphism means having many forms. In programming,
polymorphism means same function name (but different signatures) being uses for different types

"""

# Python Program to demonstrate inbulit polymorphism function

# len() can be used as a string
print('---len function used as a string----')
print()
print(len('geeks'))
print()
# len can be also used as a list
print('---len function used as a list----')
print()
print(len([10, 20, 30]))


# User-defined polymorphism

def add(x, y, z=0):
    return x + y + z


print()
print('----User Defined Polymorphism-----')
print('The first addition of 2 variables=', add(1, 2))
print('The second addition of 3 varibles=', add(1, 2, 3))

"""Polymorphism with class methods: Below code shows how python can use two different class types, in the same way. 
We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about 
which class type each object is. We assume that these methods actually exist in each class. """


class India:

    def capital(self):
        print('The capital of India is Delhi')

    def language(self):
        print('Hindi is the most spoken language in India')

    def type(self):
        print('Indian people like to talk a lot')


class America:

    def capital(self):
        print('Washington DC is the capital of America')

    def language(self):
        print('English is the most spoken language in America')

    def type(self):
        print('American people love their space and are really ambitious')


print()
obj_ind = India()
obj_us = America()

for country in (obj_ind, obj_us):
    country.capital()
    country.language()
    country.type()
    print()

"""There are four ways of implementing Polymorphism in Python:

1.Duck Typing
2.Method Overloading
3.Operator Overloading
4.Method Overriding

"""

"""1. Duck Typing:- Duck typing is a concept that says that the “type” of the object is a matter of 
concern only at runtime and you don’t need to explicitly mention the type of the object before you perform any kind 
of operation on that object, unlike normal typing where the suitability of an object is determined by its type. 

In Python, we have the concept of Dynamic typing i.e we can mention the type of variable/object later. The idea is 
that you don’t need a type in order to invoke an existing method on an object if a method is defined on it, 
you can invoke it. """

print('--------DUCK TYPING----------')
class Geeks1:
    def code(self, ide):

        ide.execute()


class Geeks2:

    def execute(self):
        print('GeeksforGeeks is the best platform for learning')


ide = Geeks2()

G1 = Geeks1()

G1.code(ide)


