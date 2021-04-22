"""Playing With Python Types, Part 1 Up until now you’ve only used basic types like str, float, and bool in your type
hints. The Python type system is quite powerful, and supports many kinds of more complex types. This is necessary as
it needs to be able to reasonably model Python’s dynamic duck typing nature.

In this section you will learn more about this type system, while implementing a simple card game. You will see how
to specify:

The type of sequences and mappings like tuples, lists and dictionaries Type aliases that make code easier to read
That functions and methods do not return anything Objects that may be of any type After a short detour into some type
theory you will then see even more ways to specify types in Python. You can find the code examples from this section
here. """

"""Example: A Deck of Cards"""

import random

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def create_deck(shuffle=False):
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    for name, cards in hands.items():
        card_str = " ".join(f"{s}{r}" for (s, r) in cards)
        print(f"{name}: {card_str}")


if __name__ == "__main__":
    play()

"""Each card is represented as a tuple of strings denoting the suit and rank. The deck is represented as a list of 
cards. create_deck() creates a regular deck of 52 playing cards, and optionally shuffles the cards. deal_hands() 
deals the deck of cards to four players. 

Finally, play() plays the game. As of now, it only prepares for a card game by constructing a shuffled deck and 
dealing cards to each player. The following is a typical output:

Sequences and Mappings Let’s add type hints to our card game. In other words, let’s annotate the functions 
create_deck(), deal_hands(), and play(). The first challenge is that you need to annotate composite types like the 
list used to represent the deck of cards and the tuples used to represent the cards themselves. 

With simple types like str, float, and bool, adding type hints is as easy as using the type itself:

Python

"""
print()
print('-----PYTHON-----')
name: str = 'Guido'
print(name)
pi: float = 3.12
print(pi)
centered: bool = True
print(centered)
# Composite Types
print()
print('--------COMPOSITE TYPE----------')
names: list = ['Guido', 'Jukka', 'Ivan']
print(names)
print(type(names))
version: tuple = (3, 7, 1)
print(version)
print(type(version))
options: dict = {'centered': False, 'capitalize': True}
print(options)
print(type(options))

"""However, this does not really tell the full story. What will be the types of names[2], version[0], and options[
"centered"]? In this concrete case you can see that they are str, int, and bool, respectively. However, 
the type hints themselves give no information about this. 

Instead, you should use the special types defined in the typing module. These types add syntax for specifying the 
types of elements of composite types. You can write the following: """
from typing import List, Dict, Tuple

print()
print('--------AFTER IMPORTING TYPING MODULE---------')
names_typing: List[str] = ['Guido', 'Jukka', 'Adil']
print(names_typing)
print(type(names_typing))
version_typing: Tuple[int, int, int] = (3, 7, 12)
print(version_typing)
print(type(version_typing))
options_1: Dict[str, bool] = {'centered': False, 'capitalize': True}
print(options_1)
print(type(options_1))

"""Note that each of these types start with a capital letter and that they all use square brackets to define item types:

names is a list of strings version is a 3-tuple consisting of three integers options is a dictionary mapping strings 
to Boolean values The typing module contains many more composite types, including Counter, Deque, FrozenSet, 
NamedTuple, and Set. In addition, the module includes other kinds of types that you’ll see in later sections. 

Let’s return to the card game. A card is represented by a tuple of two strings. You can write this as Tuple[str, 
str], so the type of the deck of cards becomes List[Tuple[str, str]]. Therefore you can annotate create_deck() as 
follows: """


def create_deck_1(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a deck of 52 Cards"""

    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


"""In addition to the return value, you’ve also added the bool type to the optional shuffle argument.

Tuples and lists are annotated differently.

A tuple is an immutable sequence, and typically consists of a fixed number of possibly differently typed elements. 
For example, we represent a card as a tuple of suit and rank. In general, you write Tuple[t_1, t_2, ..., t_n] for an 
n-tuple. 

A list is a mutable sequence and usually consists of an unknown number of elements of the same type, for instance a 
list of cards. No matter how many elements are in the list there is only one type in the annotation: List[t]. 

In many cases your functions will expect some kind of sequence, and not really care whether it is a list or a 
tuple. In these cases you should use typing.Sequence when annotating the function argument: """

# def square(elems: Sequence[float]) -> List[float]:
#    return [x ** 2 for x in elems]


# print(square(3.2))

"""Using Sequence is an example of using duck typing. A Sequence is anything that supports len() and .__getitem__(), 
independent of its actual type. 

"""

"""Type Aliases The type hints might become quite oblique when working with nested types like the deck of cards. You 
may need to stare at List[Tuple[str, str]] a bit before figuring out that it matches our representation of a deck of 
cards. 

Now consider how you would annotate deal_hands():
"""


def deal_hands_1(deck: List[Tuple[str, str]]) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]]
]:
    """Deal the card into 4 deck cards"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


"""That’s just terrible!

Recall that type annotations are regular Python expressions. That means that you can define your own type aliases by 
assigning them to new variables. You can for instance create Card and Deck type aliases: """
print()
Card = Tuple[str, str]
Deck = List[Card]
"""Card can now be used in type hints or in the definition of new type aliases, like Deck in the example above."""

"""Using these aliases, the annotations of deal_hands() become much more readable:"""


def deal_hands_2(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""

    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


"""Note that when printing Deck, it shows that it’s an alias for a list of 2-tuples of strings."""

print('-----TYPE ALIASES----')
print(Card)
print(Deck)

"""Functions Without Return Values"""

print()


def play_name(player_name):
    print(f"{player_name} plays")


shit_play = play_name('Adil')

print(shit_play)
