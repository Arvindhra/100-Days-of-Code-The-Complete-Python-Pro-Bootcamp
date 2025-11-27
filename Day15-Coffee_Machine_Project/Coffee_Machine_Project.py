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

# Add money key into the dictionary
resources.update({"money": 0})

# Create constants for the type of coins
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01

continue_ordering = True

while continue_ordering:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
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
        for key,value in resources.items():
            if key in ("water","milk"):
                print(f"{key} : {value}ml")
            elif key in ("coffee"):
                print(f"{key} : {value}g")
            elif key in ("money"):
                print(f"{key}: ${value}")
    elif coffee_choice in ('espresso','latte','cappuccino'):
        drink_choice = coffee_choice
        ingredients = MENU[drink_choice]["ingredients"]
        drink_cost = MENU[drink_choice]["cost"]
        for item,value in ingredients.items():
            if value > resources[item]:
                print(f"Sorry,there is not enough {item} 😔. We will refill it soon.")
                continue_ordering = False
                break
        if not continue_ordering:
            break
        print("Please insert coins. \nThe coins accepted would be quarters,dimes,nickels and pennies.")
        quarters_qty = int(input("How many quarters?: "))
        dimes_qty = int(input("How many dimes?: "))
        nickels_qty = int(input("How many nickels?: "))
        pennies_qty = int(input("How many pennies?: "))
        total_paid = (quarters_qty * quarter) + (dimes_qty * dime) + (nickels_qty * nickel) + \
        (pennies_qty * penny)
        if total_paid > drink_cost:
            balance = round((total_paid - drink_cost),2)
            print(f"Here is ${balance} in change. \nHere is your {drink_choice} ☕. Enjoy!")
            for item,value in ingredients.items():
                if value <= resources[item]:
                    resources[item] -= value
            resources["money"] += drink_cost
        elif total_paid == drink_cost:
            print(f"The paid amount is exactly sufficient for the {drink_choice}. \n"
                  f"Here is your {drink_choice} ☕. Enjoy!")
            for item, value in ingredients.items():
                if value <= resources[item]:
                    resources[item] -= value
            resources["money"] += drink_cost
        else:
            print(f"Sorry, that would not be enough to purchase this {drink_choice}. Money refunded.")

