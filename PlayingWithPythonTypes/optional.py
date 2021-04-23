"""The Optional Type
A common pattern in Python is to use None as a default value for an argument. This is usually done either to
avoid problems
with mutable default values or to have a sentinel value flagging special behavior.

In the card example, the player_order() function uses None as a sentinel value for start saying that if no start player
is given it should be chosen randomly:"""
from typing import Sequence, Optional

"""

def player_order(names, start=None):
    #Rotate player order so that start goes first

    if start is None:
        start_idx = names.index(start)
        return names[start_idx:] + names[:start_idx]
"""

"""The challenge this creates for type hinting is that in general start should be a string. However, it may also take 
the special non-string value None.

In order to annotate such arguments you can use the Optional type:"""


def player_order(name: str, start: Optional[str] = None) -> Sequence[str]:
    start_idx = name.index(start)
    return name[start_idx:] + name[:start_idx]


"""The Optional type simply says that a variable either has the type specified or is None. An equivalent way of 
specifying the same would be using the Union type: Union[None, str] 

Note that when using either Optional or Union you must take care that the variable has the correct type when you 
operate on it. This is done in the example by testing whether start is None. Not doing so would cause both static 
type errors as well as possible runtime errors: """

"""Note: The use of None for optional arguments is so common that Mypy handles it automatically. Mypy assumes that a 
default argument of None indicates an optional argument even if the type hint does not explicitly say so. You could 
have used the following: 

def player_order(names: Sequence[str], start: str = None) -> Sequence[str]:
    ...
If you don’t want Mypy to make this assumption you can turn it off with the --no-implicit-optional command line option.
"""

