import random
from art import logo


def random_number():
    """Return a random card from the deck of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_num = random.choice(cards)
    return cards[random_num]


def sum_value_of_cards(cards):
    sum_cards = 0
    for value in cards:
        sum_cards += value
    return sum_cards


def calculate_score(cards):
    # Hint 7
    if sum_value_of_cards(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8
    if sum_value_of_cards(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum_value_of_cards(cards)


def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []

    user_cards.append(random_number())
    user_cards.append(random_number())

    computer_cards.append(random_number())

    # Print user and computer cards array
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards}")

    # Prompt user
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # Check input
    if get_another_card == 'y':
        user_cards.append(random_number())

    computer_cards.append(random_number())

    # Print user and computer cards array
    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")

    # Calculate result
    sum_user_cards = sum_value_of_cards(user_cards)
    sum_computer_cards = sum_value_of_cards(computer_cards)

    user_diff_from_21 = 21 - sum_user_cards
    computer_diff_from_21 = 21 - sum_computer_cards

    # Display result
    if sum_user_cards > 21 or sum_computer_cards == 21:
        print("You Lose")
    elif sum_computer_cards > 21 or sum_user_cards == 21:
        print("You Win")
    elif computer_diff_from_21 < user_diff_from_21:
        print("You Lose")
    elif user_diff_from_21 < computer_diff_from_21:
        print("You Win")

    # Ask for playing again
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'y':
        blackjack_game()


blackjack_game()
