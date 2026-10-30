# This is where we will put all of our classes and their relaqted functions. 
import random

class decks:
    pass

    def shuffledeck():
        pass

class cards:
    suit = ["hearts","spades","clubs","diamonds"]
    number = ["ace","two","three","four","five","six","seven","eight","nine","ten",
              "jack","queen","king"]

    def random_card(self):
        suit = random.choice(self.suit)
        number = random.choice(self.number)
        return f"{number} of {suit}"

deck = cards()
print(deck.random_card())