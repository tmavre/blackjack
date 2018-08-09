import sys
from libs import deck
from libs import chips
from libs import hand
from libs import steps


def new_game(bet):
    # Create & shuffle the deck, deal two cards to each player
    initial_deck = deck.Deck()

    # Set up the Player's chips
    player_chips = chips.Chips()

    # Prompt the Player for their bet
    while not player_chips.take_bet(bet):
        pass

    player_hand = hand.Hand()
    player_hand.add_card(initial_deck.deal())
    player_hand.add_card(initial_deck.deal())

    dealer_hand = hand.Hand()
    dealer_hand.add_card(initial_deck.deal())
    dealer_hand.add_card(initial_deck.deal())

    init_steps = steps.Steps(
        initial_deck, player_chips, player_hand, dealer_hand)

    return init_steps


def start_game():
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

    init_steps = new_game(int(input(
        'How many chips would you like to bet? ')))

    while True:  # recall this variable from our hit_or_stand function
        init_steps.show_some()

        # Prompt for Player to Hit or Stand
        while init_steps.hit_or_stand(input(
                "Would you like to Hit or Stand? Enter 'h' or 's' ")):
            # Implement the steps of the game.
            if not init_steps.operator():
                break
            pass

        # inform Player of their chips total
        print(init_steps.show_total_chips())

        # ask to play again
        ask_for_new_game = input(
            "Would you like to play another hand? Enter 'y' or 'n' ")

        if ask_for_new_game.lower() == 'y':
            init_steps = new_game(int(input(
                'How many chips would you like to bet? ')))
            continue
        else:
            print("Thanks for playing!")
            sys.exit(0)


if __name__ == '__main__':
    start_game()
