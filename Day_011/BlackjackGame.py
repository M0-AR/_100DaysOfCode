import random

user_cards = []
computer_cards = []


def random_number():
    return random.randint(1, 53)


user_cards.append(random_number())
user_cards.append(random_number())

computer_cards.append(random_number())

print(f"Your cards: {user_cards}")
print(f"Computer's first card: {computer_cards}")

get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

if get_another_card == 'y':
    user_cards.append(random_number())
else:
    computer_cards.append(random_number())

# Todo: con -> 01:51 to make the game done.