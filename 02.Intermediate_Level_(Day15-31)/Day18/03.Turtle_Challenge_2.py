# Draw a Dashed Line

from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()