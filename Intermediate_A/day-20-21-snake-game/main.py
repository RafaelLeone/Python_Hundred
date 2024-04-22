from turtle import Screen
from snake import Snaky
from food import Food
from scoreboard import Scoreboard


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
scoreboard = Scoreboard()

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
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.snake_blocks[0].xcor() > 300 
     or snake.snake_blocks[0].xcor() < -300 
     or snake.snake_blocks[0].ycor() > 300 
     or snake.snake_blocks[0].ycor() < -300):
        game = False
        scoreboard.game_over()

    # Detect collision with tail.
    for block in list(snake.snake_blocks.values())[1:]:
        if snake.snake_blocks[0].distance(block) < 10:
            game = False
            scoreboard.game_over()

# Quit.
screen.exitonclick()
