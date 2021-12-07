# poker assignment
#figure out fold


import deck_class
import user_class
import bot_class


class Session:
    def __init__(self):
        self.pot = 0
        self.deck = deck_class.Deck()
        self.player_list = [
            user_class.User(self.deck),
            bot_class.Bot(self.deck),
            bot_class.Bot(self.deck),
            bot_class.Bot(self.deck),
        ]
        self.main()

    def flop(self, deck):
        flop_cards = []
        for i in range(3):
            flop_cards.append(deck.draw_card())
        print('---Dealer Hand---')
        for cards in flop_cards:
            cards.show()
        print('-----------------\n')

    def show_pot(self):
        print('---Pot Balance---')
        print(f'     {self.pot}$')
        print('-----------------\n')

    def ante(self, player_list, initial_bet):
        for i in player_list:
            i.balance -= initial_bet
            self.pot += initial_bet

    def main(self):
        self.ante(self.player_list, 5)
        self.show_pot()
        self.flop(self.deck)
        self.player_list[0].show_hand()


def main():
    Session()


if __name__ == '__main__':
    main()
