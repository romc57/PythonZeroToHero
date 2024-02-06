from AlphaBet import LETTERS_LIST


def encode_decode(string, shift, encode):
    new_msg = ''
    for i in range(len(string)):
        if string[i] == ' ':
            new_msg += string[i]
            continue
        index_c = LETTERS_LIST.index(string[i])
        if encode:
            new_msg += LETTERS_LIST[(index_c + shift) % len(LETTERS_LIST)]
        else:
            new_msg += LETTERS_LIST[(index_c - shift) % len(LETTERS_LIST)]
    return new_msg


def check_for_valid_str(str_input):
    for c in str_input:
        if not c.isalpha():
            return False
    return True


def get_state():
    state = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if state != 'encode' and state != 'decode':
        print('Invalid input, Exiting...')
        exit(-1)
    return state


def get_message():
    msg = input('Type your message:\n')
    if check_for_valid_str(msg):
        print('Invalid string, Exiting...')
        exit(-1)
    return msg


def get_shift():
    try:
        shift = int(input('Type your shift number:\n'))
    except:
        print('Shift can only be an integer, Exiting...')
        exit(-1)
    return shift


if __name__ == '__main__':
    go_again = 'yes'
    while go_again == 'yes':
        state = get_state()
        msg = get_message().lower()
        shift = get_shift()
        if state == 'encode':
            encoded = encode_decode(msg, shift, True)
            print('Here is your encoded result: {}\n-----------------------'.format(encoded))
        else:
            decoded = encode_decode(msg, shift, False)
            print('Here is the decoded result: {}\n-----------------------'.format(decoded))
        go_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

