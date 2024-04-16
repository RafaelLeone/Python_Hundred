from turtle import Turtle, Screen
from random import randrange


# Global constants and variables
START_LINE = -230
LAST_LANE_HEIGHT = -120
lane_height = -LAST_LANE_HEIGHT
i = 0
turtle_racers = {}

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
user_bet = screen.textinput(title="Make your bet", 
                            prompt="Which turtle will win the race? Enter a color: ")

# Character setup
while lane_height >= LAST_LANE_HEIGHT:
    r, g, b = randrange(256), randrange(256), randrange(256)
    turtle_racers['turtle_' + str(i)] = Turtle()
    turtle_racers['turtle_' + str(i)].color((r, g, b))
    turtle_racers['turtle_' + str(i)].shape("turtle")
    turtle_racers['turtle_' + str(i)].penup()
    turtle_racers['turtle_' + str(i)].goto(START_LINE, lane_height)
    lane_height -= 30
    i += 1

# Example
turtle_racers['turtle_3'].forward(100)
turtle_racers['turtle_5'].forward(200)

# Next
# Try putting the color the person chose in a random spot by
# giving it a chance to appear everytime, and if it fails,
# put it at the last lane.

# WARMUP
# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.back(10)

# def turn_left():
#     tim.left(3)

# def turn_right():
#     tim.right(3)

# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# tim = Turtle()
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
