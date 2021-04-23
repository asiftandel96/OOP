import random
import sys


class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit, ranks):
        self.suit = suit
        self.ranks = ranks

    def __repr__(self):
        return f"{self.suit}{self.ranks}"


class Deck:

    def __init__(self, cards):
        self.cards = cards

    @classmethod
    def create_deck(cls, shuffle=False):
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def deal(self, num_hands):
        """Deal the cards in the deck into a number of hands"""

        cls = self.__class__

        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def player_card(self):
        """Play a card from the player_hard"""
        card = random.choice(self.hand.cards)
        self.hand.cards.remove(card)
        print(f"{self.name}:{card!r:<3} ", end="")
        return card


class Game:

    def __init__(self, *names):
        """Set up a deck and deal cards of """
        deck = Deck.create_deck(shuffle=True)
        self.names = (list(names) + "P1 P2 P3 P4 ".split())[:4]
        self.hands = {
            n: Player(n, h) for n, h in zip(self.names, deck.deal(4))
        }

    def play(self):
        "Play a card game"

        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)

        """Play card from player hand when it is empty"""
        while self.hands[start_player].hand.cards:
            for name in turn_order:
                self.hands[name].player_card()
            print()

    def player_order(self, start=None):
        """Rotate player so that start goes first"""
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]


if __name__ == "__main__":
    # Read player names from command line
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()
