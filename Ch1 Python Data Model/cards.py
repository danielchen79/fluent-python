import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"], verbose=False)

class PokerDeck():
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

if __name__ == "__main__":
    print(Card('7', 'diamonds'))

    deck = PokerDeck()
    print(deck.ranks)
    print(deck.suits)
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(choice(deck))

    for card in deck:
        print(card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def values_of_card(card):
        rank_value = PokerDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print(Card('7', 'diamonds'))
    print(values_of_card(Card('7', 'diamonds')))
    print(deck[0])
    print(values_of_card(deck[0]))

    for card in sorted(deck, key=values_of_card):
        print(card)

    for card in deck:
        print(card)
