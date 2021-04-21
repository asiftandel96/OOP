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
