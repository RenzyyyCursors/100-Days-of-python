from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):

        for segnum in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segnum-1].xcor()
            new_y = self.segments[segnum-1].ycor()
            self.segments[segnum].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def add_segment(self):
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        lastPos = self.segments[-1].pos()
        new_segment.goto(lastPos)
        self.segments.append(new_segment)

    def check_collision(self):
        ret = True

        if not(-300 < self.segments[0].xcor() < 300) or not(-300 < self.segments[0].ycor() < 300):
            ret = False

        for segnum in range(2,len(self.segments)):
            if self.segments[0].distance(self.segments[segnum]) < 10:

                ret = False
        return ret
