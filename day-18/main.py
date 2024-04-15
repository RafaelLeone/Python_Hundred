from turtle import Turtle, Screen
from random import randrange, choice
import colorgram


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
# timmy_the_turtle.speed("fastest")
# for i in range(120):
#     r = randrange(256)
#     g = randrange(256)
#     b = randrange(256)
#     timmy_the_turtle.pencolor((r, g, b))
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.right(3)

# Hirst Challenge
CIRCLE_SIZE = 5
GAP = 50
colors = colorgram.extract('images/kirb.png', 10)
pallet = []
for color in colors:
    r = color.rgb.g
    g = color.rgb.b
    b = color.rgb.r
    pallet.append((r, g, b))
pallet.pop(0)
timmy_the_turtle.width(10)
timmy_the_turtle.speed("fastest")
timmy_the_turtle.hideturtle()
y = 300

def draw_circles(pallet):
    for i in range(9):
        color = choice(pallet)
        timmy_the_turtle.pencolor(color)
        timmy_the_turtle.pendown()
        timmy_the_turtle.circle(CIRCLE_SIZE)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(GAP)

def get_down(y):
    y -= GAP
    timmy_the_turtle.sety(y)
    return y

for i in range(10):
    timmy_the_turtle.penup()
    timmy_the_turtle.setx(-220)
    y = get_down(y)
    draw_circles(pallet)
    color = choice(pallet)
    timmy_the_turtle.pencolor(color)
    timmy_the_turtle.pendown()
    timmy_the_turtle.circle(CIRCLE_SIZE)
    timmy_the_turtle.penup()

screen.exitonclick()
