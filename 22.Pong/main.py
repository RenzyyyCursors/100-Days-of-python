from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong")
sc.tracer(0)

Rpaddle = Paddle(350, 0)
Lpaddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(Rpaddle.up, "Up")
sc.onkey(Rpaddle.down, "Down")
sc.onkey(Lpaddle.up, "w")
sc.onkey(Lpaddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    sc.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(Rpaddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.hit()

    if ball.distance(Lpaddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.hit()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.Lscore += 1
        scoreboard.showscores()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.Rscore += 1
        scoreboard.showscores()

sc.exitonclick()