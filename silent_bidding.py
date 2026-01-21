import art
print(art.logo)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


not_finished = True
bidding_data = {}
while not_finished:
    user_name = input("What is your name?:  ")
    bid = int(input("What is your bid?:  $"))
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bidding_data[user_name] = bid
    if keep_going == "yes":
        print("\n" * 100)
        continue
    else:
        not_finished = False
        find_highest_bidder(bidding_data)
        input("\nPress ENTER to exit")
