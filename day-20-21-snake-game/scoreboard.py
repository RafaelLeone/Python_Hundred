from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color((255, 255, 255))
        self.sety(260)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.setx(0)
        self.sety(-10)
        self.write("GAME OVER.", align="center", font=('Arial', 24, 'normal'))
