# Draw a Spirograph

import turtle as t
import random

timmy = t.Turtle()
timmy.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.right(gap_size)
        
draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()