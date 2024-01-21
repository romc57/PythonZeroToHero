
def hello_world():
    print("Hello world!")


def print_exercise():
    print("Day - 1\nThe function is declared like this:\nprint('What to do print')")


def string_manipulation():
    print('Hello' + ' ' + 'rom')


def print_input_len():
    print('input len is', len(input('What is your name: ')))


def get_band_name():
    city = input('Where did you grow up?\n')
    pet = input('What is your pets name?\n')
    print('Your bands name is: {}'.format(city + ' ' + pet))


if __name__ == '__main__':
    get_band_name()
