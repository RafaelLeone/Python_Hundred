from turtle import Screen, Turtle
import time


screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky")
screen.tracer(0)

# Global constants and variables
BLOCK_SIZE = 20
current_position = 0
snake_blocks = {}
game = True

for i in range(3):
    snake_blocks['turtle_' + str(i)] = Turtle()
    snake_blocks['turtle_' + str(i)].color((255, 255, 255))
    snake_blocks['turtle_' + str(i)].shape("square")
    snake_blocks['turtle_' + str(i)].penup()
    snake_blocks['turtle_' + str(i)].setx(current_position)
    current_position -= BLOCK_SIZE

while game:
    screen.update()
    time.sleep(0.1)
    for snake_block in snake_blocks:
        snake_blocks[snake_block].forward(20) 

screen.exitonclick()
