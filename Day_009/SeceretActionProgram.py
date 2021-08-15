from replit import clear
# HINT: You can call clear() to clear the output in the console.
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

# Find the winner who has maximum bid.
winnerName = ''
winnerBid = 0
for key, value in dict.items():
    if winnerBid < int(value):
        winnerName = key
        winnerBid = int(value)

# Display the winner
print(f"The winner is {winnerName} with a bid of ${winnerBid}.")
