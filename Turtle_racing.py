import random
import turtle as t

color = ["red", "yellow", "green", "orange", "purple", "brown"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
screen = t.Screen()

screen.setup(width=600, height=500)        

user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle win the race, Enter a color: ")

all_turtles = []

for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")  
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-280, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:    
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is win the race.")
            else:
                print(f"You've lost! The {winning_color} turtle is win the race.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()