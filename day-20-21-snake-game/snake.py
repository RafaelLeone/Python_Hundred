from turtle import Turtle
import time


class Snaky:
    def __init__(self):
        self.size = 3
        self.block_size = 20
        self.snake_blocks = {}

    def create_snaky(self):
        current_position = 0
        for i in range(self.size):
            self.snake_blocks[i] = Turtle()
            self.snake_blocks[i].color((255, 255, 255))
            self.snake_blocks[i].shape("square")
            self.snake_blocks[i].penup()
            self.snake_blocks[i].setx(current_position)
            current_position -= self.block_size

    def move_snaky(self):
        time.sleep(0.1)
        for i in range(self.size-1, 0, -1):
            new_x = self.snake_blocks[i-1].xcor()
            new_y = self.snake_blocks[i-1].ycor()
            self.snake_blocks[i].goto(new_x, new_y)
        self.snake_blocks[0].forward(20)
