"""Type Variables
A type variable is a special variable that can take on any type, depending on the situation.

Let’s create a type variable that will effectively encapsulate the behavior of choose():"""

import random

from typing import Sequence, TypeVar

Choosable = TypeVar('Choosable')


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


names = ['Guido', 'Jukka', 'Abido']
#reveal_type(names)

name = choose(names)
#eveal_type(name)

"""A type variable must be defined using TypeVar from the typing module. When used, a type variable ranges over all 
possible types and takes the most specific type possible. In the example, name is now a str: """
