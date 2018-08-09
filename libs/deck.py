import random
from libs import card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # build Card objects and add them to the list
                self.deck.append(card.Card(suit, rank))
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
