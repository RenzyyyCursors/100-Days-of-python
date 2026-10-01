from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0,270)
        self.score = 1

    def show_score(self):
        self.clear()
        self.write(f"Level {self.score}",align='center',font=FONT)

    def lose(self):
        self.goto(0,0)
        self.write(f"You Lose, Your score: {self.score}",align='center',font=FONT)
    
