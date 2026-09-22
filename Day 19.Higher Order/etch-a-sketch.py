from turtle import Turtle,Screen

t = Turtle()
s = Screen()

def f():
    t.forward(10)

def b():
    t.backward(10)

def r():
    t.right(10)

def l():
    t.left(10)

def up():
    t.penup()

def dp():
    t.pendown()

s.onkeypress(f,'Up')
s.onkeypress(b,'Down')
s.onkeypress(r,'Right')
s.onkeypress(l,'Left')
s.onkeypress(up,'x')
s.onkeypress(dp,'c')






s.listen()
s.exitonclick()
