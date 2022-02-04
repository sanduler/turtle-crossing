import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
cars_garage = CarManager()
current_score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

generate = 0
game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    if generate == 6:
        cars_garage.add_car()
        generate = 0
    cars_garage.movement()

    for car in cars_garage.all_cars:
        if player.distance(car) < 23:
            game_is_on = False
            current_score.game_over()

    if player.ycor() > 280:
        player.start_pos()
        current_score.increase_level()

    generate += 1

screen.exitonclick()