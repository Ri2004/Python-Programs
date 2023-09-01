from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_empty = False
while not machine_empty:
    choice = input("What would you like? (latte/espresso/cappuccino): ").lower()
    if choice == "off":
        machine_empty = True

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.get_items()
        coffee_name = menu.find_drink(choice)
        resource_sufficient = coffee_maker.is_resource_sufficient(coffee_name)
        if resource_sufficient:
            money_machine.make_payment(coffee_name.cost)
            coffee_maker.make_coffee(coffee_name)
