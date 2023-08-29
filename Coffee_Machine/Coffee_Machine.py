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
from coffee_machine_art import logo
machine_empty = False
cost = 0
print(logo)


def check_Resources_Sufficient(order_ingredients, drink):
    """Returns True if sufficient ingredients available else return False"""
    for item in order_ingredients:
        if order_ingredients[item] >= drink[item]:
            return True

        else:
            print(f"Sorry there is not enough {item}.")
            return False

def coins():
    """Return total cost entered by user"""
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennies?: "))*0.01

    return total

def is_Transaction_Successful(given_amount, drink_cost):
    """Check user give too much money against drink_cost or not, after that return True if transaction is
    successful else false"""
    if given_amount >= drink_cost:
        change = given_amount - drink_cost
        print(f"Here is ${round(change,2)} in change.")
        global cost
        cost += drink_cost
        return True

    elif given_amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_Coffee(drink_name, order_ingredients):
    """Reduce ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while not machine_empty:

    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_empty = True

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${cost}")

    else:
        drink = MENU[choice]
        if check_Resources_Sufficient(resources, drink["ingredients"]):
            payment = coins()

            if is_Transaction_Successful(payment, drink["cost"]):
                make_Coffee(choice, drink["ingredients"])
