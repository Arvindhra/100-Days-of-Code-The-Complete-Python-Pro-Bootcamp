import turtle
from turtle import Turtle,Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

df_50_states = pd.read_csv("50_states.csv")

correct_guesses = []
states_dict = df_50_states.to_dict()
states_list = df_50_states["state"].to_list()

score = 0

writer = Turtle()
writer.penup()
writer.hideturtle()

game_is_on = True

while game_is_on:
    if score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What would be your next guess?")
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What would be your next guess?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missed_guesses = [state for state in states_list if state not in correct_guesses]
        df_missing_states = pd.DataFrame(data=missed_guesses,columns=['Missing States'])
        df_missing_states.to_csv('Missing_States.csv',index=False)
        break
    for key,state in states_dict["state"].items():
        if answer_state == state and answer_state not in correct_guesses:
            score += 1
            correct_guesses.append(answer_state)
            x_cor = states_dict["x"][key]
            y_cor = states_dict["y"][key]
            writer.goto(x_cor,y_cor)
            writer.write(f"{answer_state}",align="center",font=("Times New Roman",10,"normal"))
    if score == 50:
        game_is_on = False


