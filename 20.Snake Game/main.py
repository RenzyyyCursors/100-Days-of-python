from turtle import Turtle,Screen
from food import Food,Bigfood
from snake import Snake
import time
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
food = Food(0.8, 0.8, "blue")
bigfood = Bigfood()
bigfood_timer = 0
scoreboard = Scoreboard()
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

    scoreboard.update_score()
    # Detect normal food collision
    if snake.segments[0].distance(food) < 20:
        scoreboard.score += 1
        food.refresh()
        snake.add_segment()

        # Spawn Big food every 3 points if not active
        if scoreboard.score % 3 == 0 and not bigfood.isActive:
            bigfood.spawn()
            bigfood_timer = 50  # Available for 50 ticks (~5 seconds)

    # Detect Big food collision
    if bigfood.isActive:
        bigfood_timer -= 1
        if snake.segments[0].distance(bigfood) < 25:
            scoreboard.score += 3
            bigfood.hide()
            for _ in range(2):
                snake.add_segment()
        elif bigfood_timer <= 0:
            bigfood.hide()

    if snake.check_collision() == False:
        game_is_on = False
        print("You lost")


sc.exitonclick()