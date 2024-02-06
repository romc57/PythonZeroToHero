from HangManSymbols import HANGMANPICS
from random_word import RandomWords


def get_random_word():
    r_word = RandomWords()
    print("Loading game ", end='')
    random_word = r_word.get_random_word()
    while len(random_word) != 6:
        print('.', end='')
        try:
            random_word = r_word.get_random_word()
        except:
            pass
    return random_word


def print_hangman_state(strike_num):
    if 0 <= strike_num < len(HANGMANPICS):
        print(HANGMANPICS[strike_num])
    else:
        print('invalid state')


def run_step(random_list, random_word):
    letter_input = input('Please enter a letter : ')
    if letter_input in random_word:
        print('Correct')
        random_list[random_word.index(letter_input)] = letter_input
        print(random_list)
        return True
    else:
        print('Incorrect')
        print(random_list)
        return False


if __name__ == '__main__':
    random_word = get_random_word()
    false_guesse = 0
    print('Go!')
    random_list = ["_"] * len(random_word)
    print_hangman_state(false_guesse)
    while True:
        if run_step(random_list, random_word):
            pass
        else:
            false_guesse += 1
            print_hangman_state(false_guesse)
        if len(random_word) == false_guesse:
            print('You looser!')
            break
        elif '_' not in random_list:
            print('You won! Nice.')
            break




