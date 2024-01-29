from HangManSymbols import HANGMANPICS
from random_word import RandomWords


def get_random_word():
    r_word = 'Random'
    try:
        r_word = RandomWords()
        r = r_word.get_random_word()
    finally:
        print(r_word)


def print_hangman_state(strike_num, random_word):
    if 0 <= strike_num < len(HANGMANPICS):
        print(HANGMANPICS[strike_num])
        for i in range(len(random_word)):
            pass
    else:
        print('invalid state')


def run_step(random_word):
    letter_input = input('Please enter a letter :')
    correct_count = 0
    if letter_input in random_word:
        print('Correct')
    hidden_word = ['_'] * len(random_word)
    for i in range(len(random_word)):
        word_idx = random_word.index(random_word)
        if letter_input in random_word:
            hidden_word[4] = letter_input
            print(hidden_word)
            correct_count += 1
    if correct_count != len(random_word):
        return True
    else:
        return False



if __name__ == '__main__':
    random_word = get_random_word()


