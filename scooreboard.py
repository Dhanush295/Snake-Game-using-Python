from turtle import Turtle
ALLIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.total = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.total}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALLIGNMENT, font=FONT)

    def total_score(self):
        self.total += 1
        self.clear()
        self.update_score()
