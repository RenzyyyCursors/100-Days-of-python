from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Lscore = 0
        self.Rscore = 0
        self.draw_line()
        self.showscores()

    def draw_line(self):
        line = Turtle()
        line.hideturtle()
        line.color("white")
        line.penup()
        line.goto(0, 300)
        line.setheading(270)
        for _ in range(15):
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

    def showscores(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.Lscore, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.Rscore, align="center", font=("Courier", 50, "normal"))
 

