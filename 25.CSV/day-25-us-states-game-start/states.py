import pandas
from turtle import Turtle

data = pandas.read_csv('50_states.csv')
coords = pandas.DataFrame(data)

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('Black')
        self.penup()
        self.xcoords = None
        self.ycoords = None
        self.states = []
        self.tot_list = coords.state.values.tolist()
        
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(240, 260)
        self.show_total()

    def get_position(self, state):
        self.xcoords = coords[coords.state == state].x.values[0]
        self.ycoords = coords[coords.state == state].y.values[0]
        return (self.xcoords, self.ycoords)

    def represent(self, state):
        crds = self.get_position(state)
        self.goto(crds)
        self.write(state, align='center', font=('Arial', 10, 'normal'))

    def show_total(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Score: {len(self.states)}/50", align='center', font=('Arial', 16, 'bold'))

class Timer(Turtle):
    def __init__(self, time_limit):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.time_left = time_limit
        self.is_running = True
        self.update_timer_display()

    def update_timer_display(self):
        self.clear()
        mins = self.time_left // 60
        secs = self.time_left % 60
        self.write(f"Time: {mins:02d}:{secs:02d}", align='center', font=('Arial', 16, 'bold'))
        if self.getscreen():
            self.getscreen().update()

    def start(self):
        self.countdown()

    def countdown(self):
        if self.time_left > 0 and self.is_running:
            self.time_left -= 1
            self.update_timer_display()
            self.getscreen().ontimer(self.countdown, 1000)
        elif self.time_left <= 0:
            self.is_running = False
            self.clear()
            self.write("TIME'S UP!", align='center', font=('Arial', 16, 'bold'))
            if self.getscreen():
                self.getscreen().update()




    
    