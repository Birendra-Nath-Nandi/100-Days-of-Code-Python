# Drawing Different Shapes

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(3)

colors = ["red", "green", "blue", "orange", "purple", "cyan", "gold"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.pencolor(random.choice(colors))
    draw_shape(shape_side_n)
    
screen = Screen()
screen.exitonclick()