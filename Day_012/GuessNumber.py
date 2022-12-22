import random

counter = -1
correctNumber = random.randint(1, 100)

print("logo")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
    counter = 5
else:
    counter = 10

while counter != 0:
    print(f'You have {counter} attempts remaining to guess the number.')
    userInput = int(input('Make a guess: '))
    if userInput == correctNumber:
        print(f'You got it! The answer was {correctNumber}')
        break
    elif userInput > correctNumber:
        print("Too high.")
    else:
        print("Too low.")
    counter -= 1

if counter == 0:
    print("You've run out of guesses, you lose.")
