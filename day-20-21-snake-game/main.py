from turtle import Screen, Turtle


screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky")

# Global constants and variables
BLOCK_SIZE = 20
current_position = 0
snake_blocks = {}

for i in range(3):
    snake_blocks['turtle_' + str(i)] = Turtle()
    snake_blocks['turtle_' + str(i)].color((255, 255, 255))
    snake_blocks['turtle_' + str(i)].shape("square")
    snake_blocks['turtle_' + str(i)].penup()
    snake_blocks['turtle_' + str(i)].setx(current_position)
    current_position -= BLOCK_SIZE

screen.exitonclick()
