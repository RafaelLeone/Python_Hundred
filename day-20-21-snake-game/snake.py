from turtle import Turtle
import time


class Snaky:
    def __init__(self):
        self.size = 3
        self.block_size = 20
        self.snake_blocks = {}
        self.create_snaky()

    def create_snaky(self):
        current_position = 0
        for i in range(self.size):
            current_position -= self.block_size
            self.add_block(i)

    def add_block(self, i):
        self.snake_blocks[i] = Turtle()
        self.snake_blocks[i].color((255, 255, 255))
        self.snake_blocks[i].shape("square")
        self.snake_blocks[i].penup()
        self.snake_blocks[i].setx(i)

    def extend(self):
        last_value = list(self.snake_blocks.keys())[-1]+1
        self.size += 1
        self.add_block(last_value)

    def move_snaky(self):
        time.sleep(0.06)
        for i in range(self.size-1, 0, -1):
            new_x = self.snake_blocks[i-1].xcor()
            new_y = self.snake_blocks[i-1].ycor()
            self.snake_blocks[i].goto(new_x, new_y)
        self.snake_blocks[0].forward(20)

    def up(self):
        if self.snake_blocks[0].heading() != 270:
            self.snake_blocks[0].setheading(90)
    
    def down(self):
        if self.snake_blocks[0].heading() != 90:
            self.snake_blocks[0].setheading(270)
    
    def left(self):
        if self.snake_blocks[0].heading() != 0:    
            self.snake_blocks[0].setheading(180)
    
    def right(self):
        if self.snake_blocks[0].heading() != 180:
            self.snake_blocks[0].setheading(0)
