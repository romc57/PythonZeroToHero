import os


def add_to_bid_dict(bid_dict, name, amount):
    if name in bid_dict:
        print('Error, bid was already taken for that name. Ignoring..\nTry again')
        return
    bid_dict[name] = amount


def get_bid(bid_dict):
    name = input("What is your name? ")
    try:
        amount = int(input("What is your bid?: $"))
    except:
        print('Bid should be a number. Try again')
        return True
    add_to_bid_dict(bid_dict, name, amount)
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if keep_going == 'yes':
        return True
    else:
        return False


def get_winner(bid_dict):
    highest_bid = 0
    highest_bidder = None
    for bidder in bid_dict:
        if bid_dict[bidder] > highest_bid:
            highest_bid = bid_dict[bidder]
            highest_bidder = bidder
    return highest_bidder


if __name__ == '__main__':
    print('Welcome to to the auction program')
    bids = dict()
    keep_going = True
    while keep_going:
        keep_going = get_bid(bids)
        os.system('clear')
    winner = get_winner(bids)
    print('The winner is {} with a bid of ${}'.format(winner, bids[winner]))

