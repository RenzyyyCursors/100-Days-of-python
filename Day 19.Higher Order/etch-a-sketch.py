from turtle import Turtle,Screen

t = Turtle()
s = Screen()
t.speed(0)

def f():
    t.forward(10)

def b():
    t.backward(10)

def r():
    t.right(15)

def l():
    t.left(15)

def up():
    t.penup()

def dp():
    t.pendown()

def home():
    t.penup()
    t.home()
    t.pendown()

def clc():
    t.clear()
    home()

s.onkeypress(f,'Up')
s.onkeypress(b,'Down')
s.onkeypress(r,'Right')
s.onkeypress(l,'Left')
s.onkeypress(up,'x')
s.onkeypress(dp,'c')
s.onkeypress(home,'h')
s.onkeypress(clc,'f')






s.listen()
s.exitonclick()
