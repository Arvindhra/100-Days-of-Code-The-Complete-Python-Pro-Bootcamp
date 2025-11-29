from turtle import Turtle,Screen
import random

screen = Screen()

# Set the colour mode to accept integer values from 0-255
screen.colormode(255)

# Initialize the object from the Turtle class
aamai = Turtle()

# Function to generate a random RGB tuple
def random_rgb_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


aamai.speed(2)

# Draw a triangle after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(3):
    aamai.right(120)
    aamai.forward(100)

# Now, draw a square after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(4):
    aamai.right(90)
    aamai.forward(100)

# Now, draw a pentagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(5):
    aamai.right(72)
    aamai.forward(100)

# Now, draw a hexagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(6):
    aamai.right(60)
    aamai.forward(100)

# Now, draw a heptagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(7):
    aamai.right(51.43)
    aamai.forward(100)

# Now, draw a octagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(8):
    aamai.right(45)
    aamai.forward(100)

# Now, draw a nonagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(9):
    aamai.right(40)
    aamai.forward(100)

# Now, draw a decagon after picking a random colour
aamai.color(random_rgb_colour())
for _ in range(10):
    aamai.right(36)
    aamai.forward(100)



# screen = Screen()
screen.exitonclick()

