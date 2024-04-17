from turtle import Screen
from snake import Snaky


# Screen setup.
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky")
screen.tracer(0)

# Global constants and variables.
game = True

# Create Snaky.
snake = Snaky()
snake.create_snaky()

# Move Snaky.
while game:
    screen.update()
    snake.move_snaky()

# Quit.
screen.exitonclick()
