
import random


class Bot:
    def __init__(self, deck_class):
        self.player_hand = []
        self.balance = 200
        self.draw_hand(deck_class)

    def draw_hand(self, deck_class):
        for i in range(2):
            self.player_hand.append(deck_class.draw_card())

    def show_hand(self):
        for cards in self.player_hand:
            cards.show()

    def bet(self):
        bet_size = random.randint(1, self.balance)
        return bet_size

    def fold(self):
        pass

    def call(self):
        pass

    def raize(self):
        pass

    def all_in(self):
        pass
