from turtle import Turtle,Screen
import random

t = Turtle()
t.speed(20)
colors = ["red","blue","black","green","yellow","orange","violet", "indigo", "lavender", "plum", "orchid", "fuchsia", "crimson"]
t.pensize(10)

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    clr = (r,g,b)
    return clr

for i in range(200):
    # color = random.choice(colors)
    # t.color(color)
    t.color(random_color())
    t.forward(35)
    a = random.choice([0,90,180,270])

    t.setheading(a)


screen.exitonclick()