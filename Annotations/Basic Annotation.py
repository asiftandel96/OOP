"""Annotations
Annotations were introduced in Python 3.0, originally without any specific purpose. They were simply a way to associate arbitrary expressions to function arguments and return values.

Years later, PEP 484 defined how to add type hints to your Python code, based off work that Jukka Lehtosalo had done on his Ph.D. project—Mypy. The main way to add type hints is using annotations. As type checking is becoming more and more common, this also means that annotations should mainly be reserved for type hints.

The next sections explain how annotations work in the context of type hints."""

"""Function Annotations
For functions, you can annotate arguments and the return value. This is done as follows

def func(arg: arg_type,optarg: arg_type=default) -> return_type:

For arguments the syntax is argument: annotation, while the return type is annotated using -> annotation. Note that the annotation must be a valid Python expression.

The following simple example adds annotations to a function that calculates the circumference of a circle:

"""

import math


def circumference(radius: float) -> float:
    return 2 * math.pi * radius


print(circumference(3))

print(circumference.__annotations__)

"""Sometimes you might be confused by how Mypy is interpreting your type hints. For those cases there are special 
Mypy expressions: reveal_type() and reveal_locals(). You can add these to your code before running Mypy, 
and Mypy will dutifully report which types it has inferred """

"""Even without any annotations Mypy has correctly inferred the types of the built-in math.pi, as well as our local 
variables radius and circumference. 

Note: The reveal expressions are only meant as a tool helping you add types and debug your type hints. If you try to 
run the reveal.py file as a Python script it will crash with a NameError since reveal_type() is not a function known 
to the Python interpreter. 

If Mypy says that “Name ‘reveal_locals‘ is not defined” you might need to update your Mypy installation. The 
reveal_locals() expression is available in Mypy version 0.610 and later. """

"""Variable Annotations

Variable Annotations
In the definition of circumference() in the previous section, you only annotated the arguments and the return value. You did not add any annotations inside the function body. More often than not, this is enough.

However, sometimes the type checker needs help in figuring out the types of variables as well. Variable annotations were defined in PEP 526 and introduced in Python 3.6. The syntax is the same as for function argument annotations:

"""

pi: float = 3.1432


def circumference_1(radius: float) -> float:
    return 2 * pi * radius


print(circumference_1(4))

# print(pi.__annotations__)

nothing: str
# print(nothing)
# print(dir(nothing))

"""Since no value was assigned to nothing, the name nothing is not yet defined."""

# Type Commenta
"""Type Comments As mentioned, annotations were introduced in Python 3, and they’ve not been backported to Python 2. 
This means that if you’re writing code that needs to support legacy Python, you can’t use annotations. 

Instead, you can use type comments. These are specially formatted comments that can be used to add type hints compatible with older code. To add type comments to a function you do something like this:"""


def circumference_type(radius):
    type: (float) > - float

    return 2 * math.pi * radius


print(circumference_type(2))

"""The type comments are just comments, so they can be used in any version of Python.

Type comments are handled directly by the type checker, so these types are not available in the __annotations__ dictionary:"""

print(circumference_type.__annotations__)

"""A type comment must start with the type: literal, and be on the same or the following line as the function 
definition. If you want to annotate a function with several arguments, you write each type separated by comma: """


def headline_type(text, width=80, fill_char='-'):
    type: (str, str, str) > - int

    return f"({text.title()})".center(width, fill_char)


print(headline_type("Use this type comments", width=40))
