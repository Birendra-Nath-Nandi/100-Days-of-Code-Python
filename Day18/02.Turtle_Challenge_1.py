# Draw a Square

from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(4):
    timmy.color('red')
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()