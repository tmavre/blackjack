class Hand:
    def __init__(self):
        self.cards = []  # start with an emtpy list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
                       'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                       'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
