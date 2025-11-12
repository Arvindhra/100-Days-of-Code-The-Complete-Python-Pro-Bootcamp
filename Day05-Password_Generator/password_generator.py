import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Using password in a sequence without shuffling it which means letters, symbols and numbers are arranged
# in orderly fashion.

password_list = []

for i in range(nr_letters):
    letters_to_choose = random.choice(letters)
    password_list.append(letters_to_choose)

for i in range(nr_symbols):
    symbols_to_choose = random.choice(symbols)
    password_list.append(symbols_to_choose)

for i in range(nr_numbers):
    numbers_to_choose = random.choice(numbers)
    password_list.append(numbers_to_choose)

password = ''.join(password_list)
# print(password)

# Using random shuffle to the list produced so that the letters, numbers and symbols are not in orderly
# fashion

random.shuffle(password_list)
password_ver2 = ''.join(password_list)
print(f"Your password is {password_ver2}")



