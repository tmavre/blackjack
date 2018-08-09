class Chips:
    def __init__(self):
        # This can be set to a default value or supplied by a user input
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self, bet):
        try:
            if bet > self.total:
                print("Sorry, your bet can't exceed", self.total)
                return False
            return True
        except ValueError:
            print('Sorry, a bet must be an integer!')
            return False
        finally:
            self.bet = bet
