import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0
isAnswerRight = True

# Print logo
print(logo)

while isAnswerRight:
    # Generate a random number
    a = random.randint(0, len(data) - 1)
    b = random.randint(0, len(data) - 1)
    if a == b:
        continue

    # Ask the user
    print(f'Compare A: {data[a]["name"]}, {data[a]["description"]}, {data[a]["country"]}')
    print(vs)
    print(f'Compare B: {data[b]["name"]}, {data[b]["description"]}, {data[b]["country"]}')

    answer = input("Who has more followers? Type 'A' or 'B':")

    # Check the answer
    if answer == 'A':
        isAnswerRight = data[a]["follower_count"] > data[b]["follower_count"]
    else:
        isAnswerRight = data[b]["follower_count"] > data[a]["follower_count"]

    # Display result
    if isAnswerRight:
        score += 1
        print(f'You\'re right! Current score: {score}')

# Display final result
clear()
print(logo)
print(f'Sorry, that\'s wrong. Final score: {score}')