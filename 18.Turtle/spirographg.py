from turtle import Screen,Turtle
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(150)

def rclr():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    cl = (r,g,b)
    return cl

degrees = 0
for i in range(0,120):
    t.color(rclr())
    t.circle(100)
    degrees += 3
    t.backward(1)
    t.setheading(degrees)
    

screen.exitonclick()