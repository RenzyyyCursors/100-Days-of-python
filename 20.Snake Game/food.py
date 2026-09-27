from turtle import Turtle
import random
import time

class Food(Turtle):

    def __init__(self,xs,ys,clr):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=xs,stretch_wid=xs)
        self.color(clr)
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        self.current = False

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def spawn(self):
        
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Bigfood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color('red')
        self.speed("fastest")
        self.hideturtle()
        self.goto(1000, 1000)
        self.isActive = False

    def spawn(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.showturtle()
        self.isActive = True

    def hide(self):
        self.hideturtle()
        self.goto(1000, 1000)
        self.isActive = False