from turtle import Turtle,Screen
import random

screen = Screen()
turtle = Turtle()

screen.colormode(255)

def random_rgb_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour

turtle.speed("fastest")

for _ in range(72):
    turtle.color(random_rgb_colour())
    turtle.circle(100)
    turtle.left(5)


screen.exitonclick()