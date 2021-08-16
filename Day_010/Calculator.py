from replit import clear
import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


continueWithOldResult = False
result = 0
while True:
    if not continueWithOldResult:
        clear()
        print(art.logo)
        firstNumber = int(input("What is the first number?: "))

        print("+\n-\n*\n/")
    else:
        firstNumber = result

    operation = input("Pick an operation: ")

    secondNumber = int(input("What is the next number?: "))

    if operation == '+':
        result = add(firstNumber, secondNumber)
    elif operation == '-':
        result = sub(firstNumber, secondNumber)
    elif operation == '*':
        result = mul(firstNumber, secondNumber)
    elif operation == '/':
        result = div(firstNumber, secondNumber)

    print(f"{firstNumber} {operation} {secondNumber} = {result}")

    choose = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    continueWithOldResult = choose == 'y'
