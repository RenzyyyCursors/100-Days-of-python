from turtle import Turtle,Screen

tim = Turtle()
tim.color("red")
tim.speed(1)

def fw():
    for i in range(10):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()

for i in range(4):
    tim.left(90)
    fw()









screen = Screen()
screen.exitonclick()