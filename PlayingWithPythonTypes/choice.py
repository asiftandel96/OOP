""" Any Type  """
from typing import Sequence, Any
import random


def choose(item: Sequence[Any]) -> Any:
    return random.choice(item)


"""This means more or less what it says: items is a sequence that can contain items of any type and choose() will 
return one such item of any type. Unfortunately, this is not that useful. Consider the following example: """

names = ['Gukka', 'Jukka', 'Abido']
reveal_type(names)

name = choose(names)

reveal_type(name)
