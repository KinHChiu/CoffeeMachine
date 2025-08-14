from tkinter.font import names

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_on = True
choice = ""
all_items =Menu().get_items()

while machine_on == True:
    choice = input(f"What would you like? ({all_items}) ?" ).lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = Menu().find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)