from turtle import Turtle, Screen
from random import randrange


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
screen = Screen()
screen.colormode(255)

# for i in range(25):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

CIRCLE = 360
angle = 120
sides = 3

while angle >= 36:
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    timmy_the_turtle.pencolor((r, g, b))
    for i in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
    sides += 1
    angle = CIRCLE/sides

screen.exitonclick()
