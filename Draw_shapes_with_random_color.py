import random
from turtle import Turtle, Screen
turtle = Turtle()

turtlecolors = ["DarkRed", "MediumOrchid", "OrangeRed", "DarkBlue", "DarkGoldenrod", "DodgerBlue", "magenta",
                "VioletRed2"]

def shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.right(angle)

for sides in range(3,11):
    turtle.color(random.choice(turtlecolors))
    shape(sides)

screen = Screen()
screen.exitonclick()