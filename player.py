# this is where we will keep the players class and its related functions.
from cards import cards
from cards import decks
import random

class players:

    def __init__(self, name):
        self.name = name
        self.deck = decks(f"{name}'s Deck")
        

    def drawcard(self):
        return random.choice(self.deck.cards)

    def takecards(self, opponent):
        cards_in_play = []
        while True:
            draw1 = self.drawcard()
            draw2 = opponent.drawcard()

            self.deck.cards.remove(draw1)
            opponent.deck.cards.remove(draw2)

            rank1 = cards.number.index(draw1.number)
            rank2 = cards.number.index(draw2.number)
            if rank1 > rank2:
                print(f"{draw1.card_name} is higher than {draw2.card_name}")
                self.deck.cards.extend([draw1, draw2])
                self.deck.cards.extend(cards_in_play)
                return
            elif rank2 > rank1:
                print(f"{draw2.card_name} is higher than {draw1.card_name}")
                opponent.deck.cards.extend([draw1, draw2])
                opponent.deck.cards.extend(cards_in_play)
                return
            else:
                print(f"{draw1.card_name} and {draw2.card_name} are equal. Draw again.")
                cards_in_play.extend([draw1, draw2])

