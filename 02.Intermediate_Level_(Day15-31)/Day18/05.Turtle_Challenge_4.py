# Generate a Random Walk

import turtle as t
import random

timmy = t.Turtle()
timmy.pensize(10)
timmy.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

angles = [0, 90, 180, 270]

def random_move():
    timmy.pencolor(random_color())
    timmy.setheading(random.choice(angles))
    timmy.forward(30)
    
for _ in range(200):
    random_move()

screen = t.Screen()
screen.exitonclick()