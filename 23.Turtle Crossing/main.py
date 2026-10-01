import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,'Up')
scoreboard.show_score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars(scoreboard.score)
    car_manager.move_cars()

    #Detection of collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.lose()
            game_is_on = False

    if player.level_win():
        scoreboard.score += 1
        scoreboard.show_score()
        player.goto(0, -280)
        car_manager.speed_increase()

    car_manager.clean_cars()

screen.exitonclick()