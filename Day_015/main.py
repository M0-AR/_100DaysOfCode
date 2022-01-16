MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_machine(argument):
    switcher = {
        "espresso": espresso,
        "latte": latte,
        "cappuccino": cappuccino,
        "report": report
    }
    # Get the function from switcher dictionary
    fn = switcher.get(argument, lambda: "Invalid input")
    # Invoke the selected function
    fn()


def espresso():
    water = MENU['espresso']['ingredients']['water']
    coffee = MENU['espresso']['ingredients']['coffee']
    cost = MENU['espresso']['cost']

    check_resources = enough_resources(water, 0, coffee)
    if check_resources == "ok":
        print("make espresso")
    else:
        print(f"Sorry there is not enough {check_resources}.")


def latte():
    water = MENU['latte']['ingredients']['water']
    milk = MENU['latte']['ingredients']['milk']
    coffee = MENU['latte']['ingredients']['coffee']
    cost = MENU['latte']['cost']

    check_resources = enough_resources(water, milk, coffee)

    if check_resources == "ok":
        print("make espresso")
    else:
        print(f"Sorry there is not enough {check_resources}.")


def cappuccino():
    water = MENU['cappuccino']['ingredients']['water']
    milk = MENU['cappuccino']['ingredients']['milk']
    coffee = MENU['cappuccino']['ingredients']['coffee']
    cost = MENU['cappuccino']['cost']

    check_resources = enough_resources(water, milk, coffee)

    if check_resources != "ok":
        print(f"Sorry there is not enough {check_resources}.")
    else:
        money_checking = enough_money(cost)

        if money_checking != "ok":
            print(f"Sorry that's not enough money. Money refunded.")
        else:
            print("Making cappuccino.")


def enough_resources(water, milk, coffee):
    if water > resources['water']:
        return "water"
    elif milk > resources['milk']:
        return "milk"
    elif coffee > resources['coffee']:
        return "coffee"
    else:
        return "ok"


def enough_money(cost):
    # Prompt user
    quarters = float(input("Please insert quarters: "))
    dimes = float(input("Please insert dimes: "))
    nickles = float(input("Please insert nickles: "))
    pennies = float(input("Please insert pennies: "))

    inserted_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    diff = inserted_amount - cost

    if diff > 0:
        print(f"Here is ${round(diff, 2)} dollars in change.")
        return "ok"
    elif diff == 0:
        return "ok"
    else:
        return ""


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money:")


# To turn off the Coffee Machine
off = False

while not off:
    # Prompt user
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        off = True
    else:
        coffee_machine(user_input)
