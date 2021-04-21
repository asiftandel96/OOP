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
