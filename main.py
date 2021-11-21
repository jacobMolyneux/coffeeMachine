from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
money_handler = MoneyMachine()
barista = CoffeeMaker()
# 1. get order


def runMachine():
    order = input(
        'What would you like to order? We make latte, espresso, cappuccino: ')
    if order == 'report profit':
        money_handler.report()
    elif order == 'report':
        barista.report()
    else:

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


running = True
while running == True:
    runMachine()
