"""
Level #9 Assignment: IS 303 - Hilton
Project: Python Card Game (War)

GROUP ORGANIZATION:
- 4 students total (2 pairs).
- Pair 1: Develop Card and Deck classes.
- Pair 2: Develop Player class and game play logic.
- Collaboration: Combine finished work using GitHub.

GAME RULES:
- Use two separate decks (one for each player), shuffled before starting.
- Each round: Both players draw a card. Higher card wins and collects both.
- Tie (War): Each player draws another card. Higher card wins all cards 
  played during the war. If tied again, continue the war.
- Win Condition: Play continues until one player collects all of the cards.

REQUIREMENTS & CHECKLIST:
[ ] Class: Card (represents individual cards)
[ ] Class: Deck (represents a deck of cards)
[ ] Class: Player (represents each player)
[ ] Objects: At least two Deck objects and two Player objects
[ ] Structure: A list containing multiple Card objects
[ ] Methods: Allow cards, decks, and players to interact
[ ] Loop: A game loop to continue playing rounds
[ ] Output: Messages showing round results, Wars, card counts, and the final winner
[ ] Architecture: Organize into at least 3 files (e.g., main.py, cards.py, player.py)
[ ] Execution: Program must run by executing main.py
[ ] Testing: Test normal rounds, ties, repeated ties, and the end of the game

---------------------------------------------------------

"""
# SAMPLE SESSION / OUTPUT
# ---------------------------------------------------------
# Welcome to Two-Deck War!

# Player 1 drew the 9 of Hearts.
# Player 2 drew the 4 of Spades.

# Player 1 wins the round!

# Player 1 has 53 cards.
# Player 2 has 51 cards.

# Press Enter to play the next round.

# Player 1 drew the Queen of Clubs.
# Player 2 drew the Queen of Diamonds.

# War!

# Player 1 drew the 7 of Hearts.
# Player 2 drew the 3 of Clubs.

# Player 1 wins the war!

# Player 1 has 56 cards.
# Player 2 has 48 cards.

# ...

# Player 1 has collected all of the cards.

# Player 1 wins the game!
