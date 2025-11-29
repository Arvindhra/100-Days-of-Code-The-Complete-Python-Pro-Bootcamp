from turtle import Turtle,Screen

sura = Turtle()
screen = Screen()

def move_forward():
    sura.forward(10)

def move_backward():
    sura.backward(10)

def turn_right():
    sura.right(10)

def turn_left():
    sura.left(10)

def clear_screen():
    sura.clear()
    sura.penup()
    sura.home()
    sura.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='c',fun=clear_screen)

screen.exitonclick()
