from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {round(self.score, 2)}", align= "center", font=("arial",24,"normal"))

    