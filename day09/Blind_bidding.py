
from art import logo

print(logo)
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
bidders_info = {}
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    highest_bidder = ''
    for bidder in bidding_dictionary:
        if highest_bid < bidders_info[bidder]:
            highest_bid = bidders_info[bidder]
            highest_bidder = bidder
    print("\n" * 100)
    print(f"The winner is {highest_bidder} with a bid of {highest_bid}!")

# TODO-3: Whether if new bids need to be added
to_continue = True
while to_continue :
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders_info[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == 'yes':
        to_continue = True
    elif other_bidders == 'no':
        to_continue = False
    else:
        print("You gave a wrong input! Exiting...")
        to_continue = False
    print("\n" *100)

find_highest_bidder(bidders_info)

# TODO-4: Compare bids in dictionary




