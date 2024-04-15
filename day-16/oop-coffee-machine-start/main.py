from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Choose an item from the menu:")

menu = Menu()
item = input(menu.get_items())
menu_item = menu.find_drink(item)

coffee_machine = CoffeeMaker()
coffee_machine.report()

money_machine = MoneyMachine()

print(menu_item.name)

if coffee_machine.is_resource_sufficient(menu_item):
    print("Cost: ")
    print(menu_item.cost)
    if money_machine.make_payment(menu_item.cost):
        coffee_machine.make_coffee(menu_item)

coffee_machine.report()
money_machine.report()
