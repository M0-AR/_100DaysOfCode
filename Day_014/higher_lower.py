import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0
isAnswerRight = True

# Print logo
print(logo)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_who_has_more_followers(a_followers, b_followers):
    if a_followers > b_followers:
        return 'a'
    else:
        return 'b'


while isAnswerRight:
    # Pick a random object
    a = random.choice(data)
    b = random.choice(data)

    # If two objects are same try again to pick different objects
    if a == b:
        continue

    # Ask the user
    print(f'Compare A: {format_data(a)}')
    print(vs)
    print(f'Compare B: {format_data(b)}')

    user_answer = input("Who has more followers? Type 'A' or 'B':").lower()
    correct_answer = check_who_has_more_followers(a["follower_count"], b["follower_count"])

    # Check the answer
    isAnswerRight = user_answer == correct_answer

    # Display result
    if isAnswerRight:
        score += 1
        print(f'You\'re right! Current score: {score}')

# Display final result
clear()
print(logo)
print(f'Sorry, that\'s wrong. Final score: {score}')
