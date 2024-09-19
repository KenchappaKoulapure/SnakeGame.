from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.hideturtle()
        self.update_scorebard()

    def update_scorebard(self):
        self.write(f"score : {self.score}"  , align="center" , font=("Arrial" , 15 , "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebard()