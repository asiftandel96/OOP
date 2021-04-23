import random
from typing import List, Tuple

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]


def create_deck(shuffle: bool = False) -> Deck:
    """Create a deck of 52 cards"""

    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hand(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """deal the cards in the deck into four  hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


def choose(items):
    """Choose and return an item"""

    return random.choice(items)


def player_order(names, start=None):
    """Rotate player order so that start goes first"""

    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


def play() -> None:
    """Play a 4 Card game"""

    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hand(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty

    while hands[start_player]:
        for names in turn_order:
            card = choose(hands[names])
            hands[names].remove(card)
            print(f"{names}: {card[0] + card[1]:<3}  ", end="")
        print()


if __name__ == "__main__":
    play()


"""In this example, player P3 was randomly chosen as the starting player. In turn, each player plays a card: first 
P3, then P4, then P1, and finally P2. The players keep playing cards as long as they have any left in their hand. """

