# This is the main file for our war game. This is where we will put all of our code that will run the game. 

from cards import cards
from cards import decks
from player import players


def finish_game(player1, player2):
    # Player 1 has collected all of the cards.
    if len(player1.deck.cards) == 0:
        print(f"Player 2 has collected all of the cards.")
        print(f"Player 2 wins the game!")
    elif len(player2.deck.cards) == 0:
        print(f"Player 1 has collected all of the cards.\n")
        print(f"Player 1 wins the game!")


def main():
    # initialize players and decks
    player1 = players(1)
    player2 = players(2)

    print('Welcome to Two-Deck War!')

    # start game loop
    round_count = 0
    while len(player1.deck.cards) > 0 and len(player2.deck.cards) > 0:
        player1.takecards(player2)
        print(f'Player 1 has {len(player1.deck.cards)} cards.')
        print(f'Player 2 has {len(player2.deck.cards)} cards.\n')
        input('Press Enter to play the next round.\n')

    finish_game(player1, player2)




if __name__ == "__main__":
    main()

