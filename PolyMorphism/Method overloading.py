"""Several ways to call a method (method overloading)
In Python you can define a method in such a way that there are multiple ways to call it.

Given a single method or function, we can specify the number of parameters ourself.

Depending on the function definition, it can be called with zero, one, two or more parameters.

This is known as method overloading. Not all programming languages support method overloading, but Python does."""

"""
class Hello:
    print('---Method Overloading---')
    print()

    def Say_Hello(self, name=None):

        if name is not None:
            print('Hello' + '\t' + name)
        else:
            print('Hello')


a = Hello()
# Calling the method
a.Say_Hello()
# calling the method with a parameter
a.Say_Hello('Guido')
# a.Say_Hello('Guido', 18)
"""


class Addition:

    def add(self, a=None, b=None, c=None):
        s = 0
        if (a!=None and b != None and c != None):
            s = a + b + c
        elif (a != None and b != None):
            s = a + b
        else:
            s = a
        return s


d = Addition()
print(d.add(10, 12))
print()
print(d.add(10, 12, 34))
