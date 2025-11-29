from turtle import Turtle,Screen
import random

turtle = Turtle()
screen = Screen()

screen.colormode(255)

screen.setup(600,600)
screen.screensize(600,600)

# Function to generate a random RGB tuple
def random_rgb_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

heading_angle = [0,90,180,270]

turtle.shape()

thickness = 10

BOUND_X = 290
BOUND_Y = 290

turtle_move = True

turtle.pensize(10)
turtle.speed('fastest')

while turtle_move:
    turtle.color(random_rgb_colour())
    turtle.setheading(random.choice(heading_angle))
    turtle.heading()
    turtle.forward(15)

    x, y = turtle.xcor(), turtle.ycor()

    if abs(x) > BOUND_X or abs(y) > BOUND_Y:
        turtle.right(180)
        turtle.forward(20)














screen.exitonclick()