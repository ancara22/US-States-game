from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(300, 255)

    def update_score(self, score):
        self.clear()
        self.write(f"{score}/50 States", align="center", font=("Arial", 24, "normal"))