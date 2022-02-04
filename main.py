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

screen.listen()
screen.onkey(player.go_up, "Up")

generate = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if generate == 6:
        cars_garage.add_car()
        generate = 0
    cars_garage.movement()

    for car in cars_garage.all_cars:
        if player.distance(car) < 30:
            game_is_on = False

    if player.ycor() > 280:
        player.start_pos()
    generate += 1
