from random import shuffle
l = list(range(10))
shuffle(l)
print(l)

from cards import PokerDeck
deck = PokerDeck()
print(deck)

def set_card(deck, position, card):
    deck._cards[position] = card

PokerDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])
