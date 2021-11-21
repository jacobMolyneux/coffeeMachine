from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
money_handler = MoneyMachine()
barista = CoffeeMaker()
# 1. get order
order = input(
    'What would you like to order? We make latte, espresso, cappuccino: ')

# 2. check if resources are sufficient
drink = coffee_menu.find_drink(order)

if barista.is_resource_sufficient(drink) == True:
    print('Okay i can make your drink!')
    if money_handler.make_payment(1) == True:
        barista.make_coffee(drink)
    elif money_handler.make_payment(1) == False:
        print('Oh No!')

else:
    print("Sorry, I can't make your drink")
# 3. process coins

# 4. make drink
