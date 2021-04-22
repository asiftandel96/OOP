"""Type Systems
All programming languages include some kind of type system that formalizes which categories of objects it can work with and how those categories are treated. For instance, a type system can define a numerical type, with 42 as one example of an object of numerical type.

Dynamic Typing
Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs, and that the type of a variable is allowed to change over its lifetime. The following dummy examples demonstrate that Python has dynamic typing:

"""

import mypy
def Type_checking():
    if False:
        return 1 + "two"  # This line never runs, so no TypeError is raised"

    else:
        return 1 + 2  #


a = Type_checking()
print(a)

"""def Type_checking_1():
    if True:  # Now this is type checked, and a TypeError is raised
        return 1 + "two"
    else:
        return 1 + 2


b = Type_checking_1()
print(b)
"""
"""In the first example, the branch 1 + "two" never runs so it’s never type checked. The second example shows that 
when 1 + "two" is evaluated it raises a TypeError since you can’t add an integer and a string in Python. """

"""Next, let’s see if variables can change type:"""
print('-----------Let See if variables can change type')
things = 'Hello'
print(type(things))

things = 28
print(type(things))

"""Duck Typing
Another term that is often used when talking about Python is duck typing. This moniker comes from the phrase “if it walks like a duck and it quacks like a duck, then it must be a duck” (or any of its variations).

Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than 
the methods it defines. Using duck typing you do not check types at all. Instead you check for the presence of a 
given method or attribute. """


class Hobbit:

    def __len__(self):
        return 95022


the_Hobbit = Hobbit()
print(len(the_Hobbit))

"""Hello Types In this section you’ll see how to add type hints to a function. The following function turns a text 
string into a headline by adding proper capitalization and a decorative line: """


def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()}".center(50, 'o')


"""Hello Types
In this section you’ll see how to add type hints to a function. The following function turns a text string into a headline by adding proper capitalization and a decorative line:"""
print(headline('Python Type Checking'))

print(headline('Python Type Checking', align=False))

"""It’s time for our first type hints! To add information about types to the function, you simply annotate its 
arguments and return value as follows: """

"""The text: str syntax says that the text argument should be of type str. Similarly, the optional align argument should have type bool with the default value True. Finally, the -> str notation specifies that headline() will return a string.

In terms of style, PEP 8 recommends the following:

Use normal rules for colons, that is, no space before and one space after a colon: text: str.
Use spaces around the = sign when combining an argument annotation with a default value: align: bool = True.
Use spaces around the -> arrow: def headline(...) -> str.
Adding type hints like this has no runtime effect: they are only hints and are not enforced on their own. For instance, if we use a wrong type for the (admittedly badly named) align argument, the code still runs without any problems or warnings:"""

print(headline('Python Type Checking', align="left"))
print(headline('use mypy', align="center"))
