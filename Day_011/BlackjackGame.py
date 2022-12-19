import random
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
#
#
# def sum_value_of_cards(cards):
#     sum_cards = 0
#     for value in cards:
#         sum_cards += value
#     return sum_cards
#
#
# def calculate_score(cards):
#     # Hint 7
#     if sum_value_of_cards(cards) == 21 and len(cards) == 2:
#         return 0
#     # Hint 8
#     if sum_value_of_cards(cards) > 21 and 11 in cards:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum_value_of_cards(cards)
#
#
# def blackjack_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#
#     user_cards.append(random_number())
#     user_cards.append(random_number())
#
#     computer_cards.append(random_number())
#
#     # Print user and computer cards array
#     print(f"Your cards: {user_cards}")
#     print(f"Computer's first card: {computer_cards}")
#
#     # Prompt user
#     get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#
#     # Check input
#     if get_another_card == 'y':
#         user_cards.append(random_number())
#
#     computer_cards.append(random_number())
#
#     # Print user and computer cards array
#     print(f"Your final hand: {user_cards}")
#     print(f"Computer's final hand: {computer_cards}")
#
#     # Calculate result
#     sum_user_cards = sum_value_of_cards(user_cards)
#     sum_computer_cards = sum_value_of_cards(computer_cards)
#
#     user_diff_from_21 = 21 - sum_user_cards
#     computer_diff_from_21 = 21 - sum_computer_cards
#
#     # Display result
#     if sum_user_cards > 21 or sum_computer_cards == 21:
#         print("You Lose")
#     elif sum_computer_cards > 21 or sum_user_cards == 21:
#         print("You Win")
#     elif computer_diff_from_21 < user_diff_from_21:
#         print("You Lose")
#     elif user_diff_from_21 < computer_diff_from_21:
#         print("You Win")
#
#     # Ask for playing again
#     play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if play_again == 'y':
#         blackjack_game()
#
#
# # blackjack_game()
# import math
#
# arr = []
# arr1 = []
# num = int(input("Enter number of inputs:"))
# # num=20
# # print("a".split(" "))
# for i in range(num):
#     inp = input()
#     arr.append(inp)
#
# # arr=["R 10","R 3","L 1", "R 4","L 9", "E" ,"E", "R 3", "R 3", "R 3", "E" ,"E" ,"E" ,"E" ,"E" ,"E"]
# # arr=["R 441","R 1477","E", "R 415","E", "R 5357" ,"E", "E", "R 7816", "E", "L 7724","E", "R 444","E", "R 4203","E", "L 132","E", "L 7181","E"]
# # arr=["L 6681","L 1255","R 2625", "L 1736","L 2573", "E" ,"E", "L 8141", "E", "R 7051"]
# for i in range(num):
#     a = arr[i].split(" ")
#     if len(a) > 1:
#         letter = a[0]
#         digit = int(a[1])
#     else:
#         letter = a[0]
#         digit = float('inf')
#
#     if digit != float('inf'):
#         if letter == "R":
#             arr1.append(digit)
#             # print(arr1)
#         elif letter == "L":
#             arr1.insert(0, digit)
#             # print(arr1)
#     elif digit == float('inf'):
#         if letter == "E":
#             ind = math.ceil(len(arr1) / 2) - 1
#             print(arr1.pop(ind))
#             # print(arr1)
