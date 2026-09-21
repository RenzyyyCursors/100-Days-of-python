from turtle import Turtle,Screen
import colorgram
import random

colors = colorgram.extract('istockphoto-1577713699-612x612.jpg',12)
t = Turtle()
sc = Screen()
sc.colormode(255)
t.penup()
t.goto(-300,-300)
t.speed(0)

def clr():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    cl = (r,g,b)
    return cl

for i in range(16):
    for j in range(15):
        t.color(clr())
        t.dot(20)
        t.penup()
        t.forward(40)

    t.dot(20)
    t.setheading(90)
    t.forward(40)
    if i %2 == 0:
        t.left(90)
    else:
        t.right(90)



sc.exitonclick()