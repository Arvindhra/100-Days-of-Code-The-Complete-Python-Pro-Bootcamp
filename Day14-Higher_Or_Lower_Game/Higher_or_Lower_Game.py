import random
from game_data import data
from art import logo,vs

print(logo)

continue_comparing = True

score = 0

chosen_data_1 = random.choice(data)
chosen_data_2 = random.choice([d for d in data if d != chosen_data_1])

while continue_comparing:
    statement_1 = (f"Compare A: {chosen_data_1['name']}, a {chosen_data_1['description']},"
                   f" from {chosen_data_1['country']}.")
    statement_2 = (f"Against B: {chosen_data_2['name']}, a {chosen_data_2['description']},"
                   f" from {chosen_data_2['country']}.")
    print(statement_1)
    print(vs)
    print(statement_2)
    compare_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    followers_A = chosen_data_1["follower_count"]
    followers_B = chosen_data_2["follower_count"]
    if (((followers_A > followers_B) and (compare_answer == "A")) or
            ((followers_B > followers_A) and (compare_answer == "B"))):
        score += 1
        print("\n" * 100)
        print(logo)
        print(f"You're right! Current score: {score}")
        chosen_data_1 = chosen_data_2
        chosen_data_2 = random.choice([d for d in data if d != chosen_data_1])
    else:
        final_score = score
        print("\n" * 100)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
        continue_comparing = False



