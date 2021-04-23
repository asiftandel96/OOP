import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


print(reveal_type(choose(['Guido', 'Abido', 'Jukka'])))
print(reveal_type(choose([1, 2, 3])))
print(reveal_type(choose([True, 42, 3.14])))
print(reveal_type(choose(["Python", 3, 7])))

Choosable_experiment = TypeVar('Choosable_experiment', str, int)


def choose_experiment(items: Sequence[Choosable_experiment]) -> Choosable_experiment:
    return random.choice(items)


print(reveal_type(choose_experiment(['Guido', 'Abido', 'Jukka'])))
print(reveal_type(choose_experiment([1, 2, 3.14])))
print(reveal_type(choose_experiment([True, 42, 3.14])))
print(reveal_type(choose_experiment(["Python", 3, 7])))


"""Also note that in the second example the type is considered float even though the input list only contains int 
objects. This is because Choosable was restricted to strings and floats and int is a subtype of float. """
