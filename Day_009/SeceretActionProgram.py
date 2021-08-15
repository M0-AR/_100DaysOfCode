from replit import clear
import art

# Display logo
print(art.logo)

# Define a Dictionary.
dict = {}
moreBidders = 'yes'

while moreBidders == 'yes':
    # Prompt the user to write his/her name and bid.
    userName = input("What is your name?: ")
    bid = input("What's your bid?: ")

    # Add it to the dictionary.
    dict[userName] = bid

    moreBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

# Call clear() to clear the output in the console.
clear()


# Find the winner who has maximum bid.
def find_highest_bidder(bid_record):
    winner = ''
    highest_bid = 0
    for key, value in bid_record.items():
        if highest_bid < int(value):
            winner = key
            highest_bid = int(value)
    return winner, highest_bid


winnerName, winnerBid = find_highest_bidder(dict)
# Display the winner
print(f"The winner is {winnerName} with a bid of ${winnerBid}.")
