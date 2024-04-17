from turtle import Screen
from snake import Snaky
from food import Food


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
food = Food()

# Control Snaky
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Move Snaky.
while game:
    screen.update()
    snake.move_snaky()

    # Detect collision with food.
    if snake.snake_blocks[0].distance(food) < 21:
        food.refresh()

# Quit.
screen.exitonclick()
