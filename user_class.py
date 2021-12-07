
from deck_class import Deck


class User:
    def __init__(self, deck_class):
        self.player_hand = []
        self.balance = 200
        self.draw_hand(deck_class)

    def draw_hand(self, deck_class):
        for i in range(2):
            self.player_hand.append(deck_class.draw_card())

    def show_hand(self):
        print('-----------------')
        print('Your Hand:')
        for cards in self.player_hand:
            cards.show()
        self.show_balance()
        print('-----------------')
        print('optione')

    def show_balance(self):
        print(f'Balance: {self.balance}$')
        return self.balance

    def fold(self):
        pass

    def call(self):
        pass

    def raize(self):
        pass

    def all_in(self):
        pass
