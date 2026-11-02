# This is where we will put all of our classes and their relaqted functions. 
import random

# Define the classes for cards and decks
class decks:
    

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.fill_deck()



# Define a method to fill the deck with all cards
    def fill_deck(self):
        self.cards = []
        for suit in cards.suit:
            for number in cards.number:                
                card = cards(suit, number, f"{number} of {suit}")
                self.cards.append(card)




# Define a method to shuffle the deck
    def shuffledeck(self):
        random.shuffle(self.cards)


# Define the class for individual cards
class cards:
    suit = ["hearts","spades","clubs","diamonds"]
    number = ["two","three","four","five","six","seven","eight","nine","ten",
                    "jack","queen","king", "ace"]

    def __init__(self, suit, number, card_name):
        self.suit = suit
        self.number = number
        self.card_name = card_name
        

# Define a method to get a random card from the deck
    def random_card(self):
        suit = random.choice(self.suit)
        number = random.choice(self.number)
        return f"{number} of {suit}"


deck1 = decks("Deck 1")
print(deck1.cards)




