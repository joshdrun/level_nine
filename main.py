# This is the main file for our war game. This is where we will put all of our code that will run the game. 

from cards import cards
from cards import decks
from player import players

def hand_check():
    # Player 1 has 53 cards.
    # Player 2 has 51 cards.
    pass

def finish_game():
    # Player 1 has collected all of the cards.

    # Player 1 wins the game!
    pass

def main():

    player1 = players(1)
    player2 = players(2)


    print('Welcome to Two-Deck War!')

    # start game loop
    # while len(player1.deck.cards) > 0 and len(player2.deck.cards) > 0:
    #     player1.takecards(player2)

        #players draw

        # player1_card = player1.drawcard()
        # player2_card = player2.drawcard()


        # # Player 1 drew the 9 of Hearts.
        # # Player 2 drew the 4 of Spades.

        # print(f"\nPlayer 1 drew the {player1_card.number} of {player1_card.suit}.")
        # print(f"\nPlayer 2 drew the {player2_card.number} of {player2_card.suit}.")

        
        #blank print
        #print # Player 1 wins the round!

        #hand check function

        #blank print
        # press enter to play the next round
    
    #finish game func



if __name__ == "__main__":
    main()

