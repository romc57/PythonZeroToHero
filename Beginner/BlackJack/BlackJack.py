import random


CARDS = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
DECKS = 6


def get_new_deck():
    cards = list()
    for i in range(DECKS):
        for card in CARDS:
            cards.append(card)
    random.shuffle(cards)
    return cards


def get_new_card():
    pass


def play_round():
    pass


if __name__ == '__main__':
    print(get_new_deck())