# Turtle Graphics

# Documentation - https://docs.python.org/3/library/turtle.html
# Turtle Color - https://cs111.wellesley.edu/reference/colors

import turtle

timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("Blue")
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()