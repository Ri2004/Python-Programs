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

def showReport(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    resources["Money"] = "$0"
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {resources['Money']}"

def coins():
    quarter = float(input("how many quarters?: "))  # 1 quarter = 25 cents 0.25
    dime = float(input("how many dimes?: "))  # 1 dime = 10 cents 0.10
    nickel = float(input("how many nickels?: "))  # 1 nickel = 5 cents 0.05
    penny = float(input("how many pennies?: "))  # 1 penny = 1 cent 0.01
    monetary_calculation = ((0.25 * quarter) + (0.10 * dime * 2) + (0.05 * nickel) + (0.01 * penny * 2))

    return monetary_calculation

machine_empty = False
while not machine_empty:
    ask_user = input("​What would you like? (espresso/latte/cappuccino): ")
    if ask_user == "report":
        report = showReport(resources)
        print(report)

    elif ask_user == "espresso":
        print("Please insert coins.")
        monetary_calculation = coins()
        cost = MENU["espresso"]["cost"]

        if monetary_calculation < cost:
            print("Sorry that's not enough money. Money refunded.")
        elif monetary_calculation > cost :
            change = round(monetary_calculation - cost,2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso ☕️. Enjoy!")
        else:
            print("Here is your espresso ☕️. Enjoy!")

        water_reduce = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        coffee_reduce = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["water"] = water_reduce
        resources["coffee"] = coffee_reduce

    elif ask_user == "latte":
        print("Please insert coins.")
        monetary_calculation = coins()
        cost = MENU["latte"]["cost"]
        if monetary_calculation < cost:
            print("Sorry that's not enough money. Money refunded.")
        elif monetary_calculation > cost :
            change = round(monetary_calculation - cost,2)
            print(f"Here is ${change} in change.")
            print("Here is your latte ☕️. Enjoy!")
        else:
            print("Here is your latte ☕️. Enjoy!")

        water_reduce = resources["water"] - MENU["latte"]["ingredients"]["water"]
        coffee_reduce = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        milk_reduce = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

        resources["water"] = water_reduce
        resources["coffee"] = coffee_reduce
        resources["milk"] = milk_reduce

    elif ask_user == "cappuccino":
        print("Please insert coins.")
        monetary_calculation = coins()
        cost = MENU["cappuccino"]["cost"]
        if monetary_calculation < cost:
            print("Sorry that's not enough money. Money refunded.")
        elif monetary_calculation > cost:
            change = round(monetary_calculation - cost, 2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Here is your cappuccino ☕️. Enjoy!")

        water_reduce = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        coffee_reduce = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        milk_reduce = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]

        resources["water"] = water_reduce
        resources["coffee"] = coffee_reduce
        resources["milk"] = milk_reduce

    elif ask_user == "off":
        machine_empty = True