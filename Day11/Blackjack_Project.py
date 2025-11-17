from art import logo
import random

def calculate_score(cards):
    total_score = sum(cards)
    while total_score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        total_score = sum(cards)
    return total_score

def get_choice(prompt,options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print("Invalid option. Try again!")

num_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print(logo)

continue_playing = True

while continue_playing:

    user_choice = get_choice("Do you want to play a game of Blackjack? Type 'y' or 'n': ",('y','n'))

    if user_choice == 'y':
       user_cards = random.sample(num_list,2)
       computer_cards = random.sample(num_list,2)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Check for blackjack from the first two cards.
    if user_score == 21 or computer_score == 21:
        print(f"\tYour cards: {user_cards},final_score: {user_score}")
        print(f"\tComputer's cards: {computer_cards},final_score: {computer_score}")
        if user_score == 21 and computer_score == 21:
            print("Both got Blackjack! It's a draw!🤝")
        elif user_score == 21:
            print("You got the Blackjack! You won!😄")
        else:
            print("Computer got the Blackjack! Computer wins!😥")
        continue


    if user_choice == 'n':
       print("Thank you for playing. Have a great day ahead! 👋")
       continue_playing = False
       # break

    print(f"\tYour cards: {user_cards}, current_score: {user_score}")
    print(f"\tComputer's first_card: {computer_cards[0]}")
    # print(computer_cards)

    player_turn = True

    while player_turn:

        player_turn_reply = get_choice("Type 'y' to get another card, type 'n' to pass: ",('y','n'))

        if player_turn_reply == 'y':
            next_user_card = random.choice(num_list)
            user_cards.append(next_user_card)
            user_score = calculate_score(user_cards)
            if user_score > 21:
                print("User goes over 21. User lost!😥")
                player_turn = False
        elif player_turn_reply == 'n':
            player_turn = False

        print(f"\tYour cards: {user_cards}, current_score: {user_score}")
        print(f"\tComputer's first_card: {computer_cards[0]}")


    while user_score <= 21 and computer_score < 17:
        next_computer_card = random.choice(num_list)
        computer_cards.append(next_computer_card)
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, current score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")


    if user_score > 21:
        print("User goes over 21. User lost!😥")
    elif computer_score > 21:
        print("Computer goes over 21. User wins!😄")
    elif user_score > computer_score:
        print("You win.😄")
    elif computer_score > user_score:
        print("Computer wins.😥")
    else:
        print("It's a draw.🤝")




    # print(computer_cards[1])