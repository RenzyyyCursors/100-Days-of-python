#%%
from turtle import Turtle,Screen
import random

t = Turtle()
t.speed(2)

colors = ["red","blue","black","green","yellow","orange","violet", "indigo", "lavender", "plum", "orchid", "fuchsia", "crimson"]

for i in range(3,11):
    tot = 360/i
    curr_color = random.choice(colors)
    t.color(curr_color)
    for i in range(i):
        t.forward(100)
        t.left(tot)

screen = Screen()
screen.exitonclick()
# %%
