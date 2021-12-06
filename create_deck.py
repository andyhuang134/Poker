# create the card
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        # prints out the card in string format
        print(f'{self.value} of {self.suit}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in ['Diamonds', 'Spades', 'Clubs', 'Hearts']:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
        random.shuffle(self.cards)

    def show_card(self):
        for cards in self.cards:
            cards.show()
        # print(self.cards[0].__dict__) --> ["suit": ,"value": ] of card

    def draw_card(self):
        return self.cards.pop()