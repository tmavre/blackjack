class Steps:
    def __init__(self, deck, chips, player_hand, dealer_hand):
        self.chips = chips
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand

    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.adjust_for_ace()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.adjust_for_ace()

    def hit_or_stand(self, get_hit_or_stand):
        if get_hit_or_stand.lower() == 'h':
            self.hit()
            return True

        elif get_hit_or_stand.lower() == 's':
            print("Player stands. Dealer is playing.")
        else:
            print("Sorry, please try again.")
        return True

    def operator(self):
        # If player's hand exceeds 21,
        # run player_busts() and break out of loop
        if self.player_hand.value > 21:
            self.player_busts()
            self.show_all()
            return False

        # If Player hasn't busted, play Dealer's
        # hand until Dealer reaches 17
        if self.player_hand.value <= 21:

            while self.dealer_hand.value <= 17:
                self.hit()

            # Run different winning scenarios
            if self.dealer_hand.value > 21:
                self.dealer_busts()

            elif self.dealer_hand.value > self.player_hand.value:
                self.dealer_wins()

            elif self.dealer_hand.value < self.player_hand.value:
                self.player_wins()

            else:
                print("Dealer and Player tie! It's a push.")

        # Show all cards
        self.show_all()
        return False

    def show_total_chips(self):
        return "\nPlayer's winnings stand at " + str(self.chips.total)

    def show_some(self):
        print("\nDealer's Hand:")
        print("<card is hidden>")
        print('', self.dealer_hand.cards[1])
        print("\nPlayer's Hand:", *self.player_hand.cards, sep='\n ')

    def show_all(self):
        print("\nDealer's Hand:", *self.dealer_hand.cards, sep='\n ')
        print("Dealer's Hand =", self.dealer_hand.value)
        print("\nPlayer's Hand:", *self.player_hand.cards, sep='\n ')
        print("Player's Hand =", self.player_hand.value)

    def player_busts(self):
        print("----------- Player busts -----------")
        self.chips.lose_bet()

    def player_wins(self):
        print("----------- Player wins! -----------")
        self.chips.win_bet()

    def dealer_busts(self):
        print("----------- Dealer busts -----------")
        self.chips.win_bet()

    def dealer_wins(self):
        print("----------- Dealer wins! ----------- ")
        self.chips.lose_bet()
