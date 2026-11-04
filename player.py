# imports cards and decks class from cards.py and imports random
from cards import cards
from cards import decks
import random

#creates the class players
class players:

#Creates the constructor for the players class. Takes the name and creates a 
#deck for the player using the decks class from cards.py
    def __init__(self, name):
        self.name = name
        self.deck = decks(f"{name}'s Deck")
        
#A method that draws a card the first or "top card" from a player's deck
    def drawcard(self):
        return self.deck.cards[0]

#A method that takes the cards from the player and the opponent and compares
#the rank of the cards.
    def takecards(self, opponent):
        #Creates an empty list to hold the cards that are in play during a tie.
        cards_in_play = []
        #starts a while loop that will continue until one player wins the round.
        while True:
            #Makes the players draw a card from their respective decks.
            draw1 = self.drawcard()
            draw2 = opponent.drawcard()

            #Removes the drawn cards from the players' decks.
            self.deck.cards.remove(draw1)
            opponent.deck.cards.remove(draw2)

            #Gets the rank of the drawn cards by finding the index of the card's
            #number in the cards.number list.
            rank1 = cards.number.index(draw1.number)
            rank2 = cards.number.index(draw2.number)

            #Compares the ranks of the drawn cards and determines the winner
            #If player 1's card is higher, it will extend player 1's deck
            #with the drawn cards and any cards that were in play during a tie
            if rank1 > rank2:
                # print(f"{draw1.card_name} is higher than {draw2.card_name}")
                self.deck.cards.extend([draw1, draw2])
                self.deck.cards.extend(cards_in_play)
                return
            #If player 2's card is higher, it will extend player 2's deck
            #with the drawn cards and any cards that were in play during a tie
            elif rank2 > rank1:
                # print(f"{draw2.card_name} is higher than {draw1.card_name}")
                """Dylan - I changed the order of the cards being added to the opponents deck to prevent an infinite game loop."""
                opponent.deck.cards.extend([draw2, draw1])
                opponent.deck.cards.extend(cards_in_play)
                return
            #If the cards are equal, it will add the drawn cards to the cards_in_play
            #list and prints a message that the cards are equal and to draw again.
            else:
                # print(f"{draw1.card_name} and {draw2.card_name} are equal. Draw again.")
                cards_in_play.extend([draw1, draw2])
                """Dylan - I added this check to prevent an infinite game loop if one player runs out of cards during a tie. If either player has no cards left, the function will return and the game will end."""
                if len(self.deck.cards) == 0:
                    opponent.deck.cards.extend(cards_in_play)
                    return
                elif len(opponent.deck.cards) == 0:
                    self.deck.cards.extend(cards_in_play)
                    return

