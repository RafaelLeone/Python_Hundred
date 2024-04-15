from turtle import Turtle, Screen
from random import randrange, choice


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
screen = Screen()
screen.colormode(255)

# CHALLENGE 2
# for i in range(25):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

# CHALLENGE 3
# CIRCLE = 360
# angle = 120
# sides = 3
# while angle >= 36:
#     r = randrange(256)
#     g = randrange(256)
#     b = randrange(256)
#     timmy_the_turtle.pencolor((r, g, b))
#     for i in range(sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#     sides += 1
#     angle = CIRCLE/sides

# CHALLENGE 4
# choices = [0, 90, 270]
# timmy_the_turtle.speed("fast")
# for i in range(100):
#     r = randrange(256)
#     g = randrange(256)
#     b = randrange(256)
#     timmy_the_turtle.pencolor((r, g, b))
#     timmy_the_turtle.width(5)
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.right(choice(choices))

# CHALLENGE 5
timmy_the_turtle.speed("fastest")
for i in range(120):
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    timmy_the_turtle.pencolor((r, g, b))
    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(3)

screen.exitonclick()
