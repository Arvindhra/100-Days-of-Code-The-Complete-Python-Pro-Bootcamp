import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Make sure the user choice is between 0, 1 and 2
if user_choice >= 0 and user_choice <= 2:
    print(game_options)
else:
    print("Number is invalid for the game.Try again!")

# Build the computer choice codes
computer_choice = random.randint(0,2)
print(computer_choice)
print(game_options[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice == 0 and computer_choice == 1:
    print("You lose.")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 1 and computer_choice == 0:
    print("You win.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice == 2 and computer_choice == 1:
    print("You win.")
elif user_choice == computer_choice:
    print("The game is drawn.")
else:
    print("Something seems off here, but you still lose, anyway.")


