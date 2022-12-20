import random
from replit import clear
from art import logo


def deal_card():
    """Return a random card from the deck of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 5: Deal the user and computer 2 cards each using deal_card()
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


# 6
def calculate_score(cards):
    # 7
    if check_balckjack(cards):
        return 0
    # 8
    if check_for_ace(cards) and sum(cards) > 21:
        replace_ace_by(cards, 1)
    return sum(cards)


# 7
def check_balckjack(cards):
    return check_for_ace(cards) and 10 in cards and len(cards)


# 8
def check_for_ace(cards):
    return 11 in cards


def replace_ace_by(cards, replacement):
    cards.remove(11)
    cards.append(replacement)


# 9
def end_of_game(user_score, computer_score):
    return user_score > 21 or user_score == 0 or computer_score == 0


# 13
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


# 10 + 11
def play_game():
    print(logo)
    is_game_over = False
    user_score = 0
    computer_score = 0
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        is_game_over = end_of_game(user_score, computer_score)
        # 10
        if not is_game_over:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 12
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# 14
while input("Do you want to play a game of Blackjack? Typ 'y' or 'n': ") == "y":
    clear()
    play_game()