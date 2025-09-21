# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

name_bid = {}

continue_bidding = True

while continue_bidding:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid? : RM"))

    valid_choice = False

    while not valid_choice:
        choice = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()

        if choice in ('yes','no'):
            name_bid[name] = bid
            valid_choice = True
        else:
            print('Invalid input. You can only type yes or no for this question.')

    print('\n' * 100)

    if choice == 'no':
        continue_bidding=False

max_bid_person= max(name_bid,key=name_bid.get)
highest_bid_value = name_bid[max_bid_person]
print(f"The winner of the bid is {max_bid_person} with RM{highest_bid_value}.")






