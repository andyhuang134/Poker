# poker assignment

import deck_class
import user_class
import bot_class


class PreloadGame:
    pass


class Session:
    def __init__(self):
        self.pot = 0


def main():
    deck = deck_class.Deck()
    player_list = [
        user_class.User(deck),
        bot_class.Bot(deck),
        bot_class.Bot(deck),
        bot_class.Bot(deck)
    ]


if __name__ == '__main__':
    main()
