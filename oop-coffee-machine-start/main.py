from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        selected_coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(selected_coffee):
            if money_machine.make_payment(selected_coffee.cost):
                coffee_maker.make_coffee(selected_coffee)