from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.hits = 0
        self.hideturtle()

    def update_score(self): 
        self.clear()
        self.write(f"Score: {round(self.score, 2)}", align= "center", font=("arial",12,"normal"))

    def highscore(self):
        with open('data.txt','r') as f:
            lines = f.readlines()
            current_high = int(lines[0].strip())

        if current_high < self.score:
            str_score = f"{self.score}"
            lines[0] = str_score
            with open('data.txt','w') as f:
                f.writelines(lines)

    def lost_display(self,scr,high_scr):
        lost = Turtle()
        lost.color("White")
        lost.penup()
        lost.hideturtle()
        lost.write(f"You lost, Score: {scr}; High Score: {high_scr}",align='center',font=("arial",24,'normal'))



    