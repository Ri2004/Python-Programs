import random
import turtle
t = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

turtle.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)
s = turtle.exitonclick()