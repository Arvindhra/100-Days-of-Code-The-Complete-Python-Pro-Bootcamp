from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

check_answer = True

while check_answer:
    user_choice = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()

    if user_choice in ('easy','hard'):
        check_answer = False
    else:
        print("Invalid option. Try again.")

# numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
#                 26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
#                 51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,
#                 76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#
# chosen_number = random.choice(numbers_list)

chosen_number = random.randint(1,100)

# print(chosen_number)

if user_choice == 'easy':
    lives = 10
elif user_choice == 'hard':
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")
user_guess = int(input("Make a guess: "))

continue_game = True

while continue_game:
    if user_guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}")
        continue_game = False
    elif user_guess > chosen_number:
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            continue_game = False
        else:
            print(f"Too high. \nGuess again. \nYou have {lives} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
    elif user_guess < chosen_number:
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            continue_game = False
        else:
            print(f"Too low. \nGuess again. \nYou have {lives} attempts to guess the number.")
            user_guess = int(input("Make a guess: "))


