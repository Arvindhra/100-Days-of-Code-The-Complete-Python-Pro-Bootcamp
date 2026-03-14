from turtle import Turtle

SCORE = 0
ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0,270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score = {SCORE}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.clear()
        global SCORE
        SCORE += 1
        self.write(f"Score = {SCORE}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over!", align = ALIGNMENT, font = FONT)
