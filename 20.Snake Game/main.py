from turtle import Turtle,Screen
from snake import Snake
import time

sc = Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
game_is_on = True

sc.listen()
sc.onkey(snake.right,"Right")
sc.onkey(snake.left,"Left")
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")

while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()


sc.exitonclick()