from turtle import Turtle,Screen
import random

sc = Screen()
sc.setup(width=500,height=400)

user_bet = sc.textinput(title="Make your bet",prompt="Which color will win the race?")
colors = ["indianred", "forestgreen", "turquoise", "darkorchid", "gold", "lightsalmon"]
yPos = [-125,-75,-25,25,75,125]
all_turtles = []

for tIdx in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[tIdx])
    t.penup()
    t.goto(x=-225,y=yPos[tIdx])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            if turtle.pencolor() == user_bet:
                print(f"You've won bet! {turtle.pencolor()} won")
                is_race_on = False
            else:
                print(f"You've lot bet! {turtle.pencolor()} won")
                is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)






sc.exitonclick()