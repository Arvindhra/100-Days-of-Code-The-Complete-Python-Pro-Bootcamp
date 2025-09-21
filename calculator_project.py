from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

calculator_on = True
while calculator_on:
    print(logo)
    first_number = float(input("What's the first number?: "))
    continue_calculation = True

    while continue_calculation:
        for key in operations:
            print(key)
        chosen_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        if chosen_operation in operations:
            result = operations [chosen_operation] (first_number,second_number)
            print(f"{first_number} {chosen_operation} {second_number} = {result}")
        else:
            print('Invalid operation.Try again!')

        while True:

            user_reply = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation \n"
                               f"or type 'exit' to exit the calculator program : ").lower()

            if user_reply in ('y','n','exit'):
                break
            else:
                print('Invalid choice. Try again.')

        if user_reply == 'y':
            first_number = result
        elif user_reply == 'n':
            continue_calculation = False
            print('\n' * 100)
        elif user_reply == 'exit':
            continue_calculation = False
            calculator_on = False