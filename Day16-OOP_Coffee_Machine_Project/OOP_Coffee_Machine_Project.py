from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

continue_ordering = True

while continue_ordering:
    coffee_options = menu.get_items()
    coffee_choice = input(f"What would you like? ({coffee_options}): ")
    check_coffee_choice = True
    while check_coffee_choice:
        if coffee_choice not in ('espresso','latte','cappuccino','report','maintenance'):
            print("Your choice is invalid. Please try again.")
            check_coffee_choice = False
        else:
            check_coffee_choice = False
    if coffee_choice == 'maintenance':
        maintenance_answer = input("Do you want to turn off the machine to repair it? Type 'off' for confirmation: ")
        if maintenance_answer == 'off':
            print("Machine will be turned off for maintenance.😴")
            continue_ordering = False
        else:
            print("The input is wrong. The machine will not be turned off and will continue serving the customer.")
    elif coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif coffee_choice in ('espresso', 'latte', 'cappuccino'):
        item_chosen = menu.find_drink(coffee_choice)
        sufficient_or_not = coffee_maker.is_resource_sufficient(item_chosen)
        if not sufficient_or_not:
            break
        payment_status = money_machine.make_payment(item_chosen.cost)
        if not payment_status:
            continue
        coffee_maker.make_coffee(item_chosen)









