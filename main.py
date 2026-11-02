# This is the main file for our war game. This is where we will put all of our code that will run the game. 
from cards import cards
from cards import decks
from player import players

player1 = players(input("Player 1, please enter your name: "))
player2 = players(input("Player 2, please enter your name: "))

player1.takecards(player2)

#test1 = deck1.cards.index(deck1.cards[48])
#test2 = deck1.cards.index(deck1.cards[30])
#if test1 > test2:
#    print(f"{deck1.cards[test1].card_name} is higher than {deck1.cards[test2].card_name}")
#else:
#    print(f"{deck1.cards[test2].card_name} is higher than {deck1.cards[test1].card_name}")
