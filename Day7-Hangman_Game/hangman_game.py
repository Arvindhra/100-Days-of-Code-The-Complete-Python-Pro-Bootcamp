import random

from hangman_art import logo, stages
print(logo)

from hangman_wordlist import word_list
chosen_word = random.choice(word_list)

placeholder = ''

for letter in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

correct_guesses = []

game_over = False

lives = 6

while not game_over:
    guess = input("Guess the letter: ").lower()

    display = ''

    if guess in correct_guesses:
        print(f"You have already guessed the letter {guess}. Try again.")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += '_'

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the chosen word. You lose a life.")

    print(display)
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(stages[lives])

    if lives == 0:
        game_over = True
        print("THE CORRECT WORD WAS " + chosen_word + ". YOU LOSE!")

    if '_' not in display:
        game_over = True
        print("All the letters have been guessed correctly. \n"
              "The word is " + display + ". YOU WIN!")
