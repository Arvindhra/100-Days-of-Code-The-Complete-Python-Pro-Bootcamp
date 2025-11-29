import colorgram
from turtle import Turtle,Screen
import random

colors = colorgram.extract("spot_image.png",33)
# number_of_colors = len(colors)
# print(number_of_colors)

def rgb_tuple(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    rgb_color = (r,g,b)
    return rgb_color

color_list = []

for color in colors:
    rgb_details = color.rgb
    rgb_values = rgb_tuple(rgb_details)
    color_list.append(rgb_values)

# The output of the rgb colours from the image is inserted down below.

color_tuples = [(0, 0, 0), (162, 164, 168), (168, 164, 156), (157, 169, 164), (172, 156, 165), (185, 158, 46), (63, 91, 153), (166, 67, 38), (223, 211, 106), (73, 24, 42), (163, 26, 54), (56, 124, 70), (157, 34, 33), (142, 75, 121), (224, 167, 191), (31, 62, 40), (133, 117, 173), (27, 30, 48), (184, 188, 212), (67, 145, 159), (110, 159, 67), (226, 231, 226), (55, 70, 38), (158, 107, 122), (204, 205, 214), (170, 106, 95), (53, 71, 47), (162, 199, 211), (59, 61, 73), (194, 190, 189), (186, 196, 186)]

turtle = Turtle()
screen = Screen()

screen.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")

x_pos = -250
y_pos = -250

turtle.teleport(x_pos,y_pos)


for _ in range(110):
    if _ % 11 == 0:
        y_pos += 50
        turtle.teleport(x_pos,y_pos)
    else:
        turtle.dot(20,random.choice(color_tuples))
        turtle.forward(50)


screen.exitonclick()
