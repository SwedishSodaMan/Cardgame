from enum import Enum
from enum import IntEnum


The_entire_deck = []
Player1cards = []
Player2cards = []

# Card enum for playing the cards

class Card(IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


# Class to suit enum for playing cards
class Suit(Enum):
    spades = 'spades'
    clubs = 'clubs'
    hearts = 'hearts'
    diamonds = 'diamonds'


# Class made to hold the information for playing the cards
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

def create_deck():
    for suit in Suit: 
        for card in Card:
         The_entire_deck.append(PlayingCard(Card(card), Suit(suit)))
    return The_entire_deck

if __name__ == "__main__":
    main()