# Name: Ruben Sanduleac
# Date: February 4th, 2022
# Description: Turtle crossing is a replica of the classic Frogger game
#              developed in 1981. The goal of the game is to get the player - turtle -
#              across without getting hit by an object.
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# generate a screen object
screen = Screen()
# set the dimensions of the window
screen.setup(width=600, height=600)
# set the background color of the window
screen.bgcolor("black")
screen.tracer(0)
# initialize a player, cars_garage, and current_score objects from the respective classes
player = Player()
cars_garage = CarManager()
current_score = Scoreboard()

# screen listen for the a key press
screen.listen()
screen.onkey(player.go_up, "Up")
# counter used to generate cars once every 6 iterations.
generate = 0
# keep playing while the game is true
game_is_on = True
while game_is_on:
    # pass the speed of the game to the player class to be used later
    # to increase in dificulty
    time.sleep(player.move_speed)
    # update the screen
    screen.update()
    # if statmentent used to generate cars every 6 iterations,
    # once completed a car object is created and generate is reset to 0.
    if generate == 6:
        cars_garage.add_car()
        generate = 0
    # move the cars
    cars_garage.movement()

    # colision detection by looping through all the cars in the list of
    # then checking if they are less that 23 pixel away from the player
    for car in cars_garage.all_cars:
        if player.distance(car) < 23:
            game_is_on = False
            current_score.game_over()
    # check to see if the player is on the other side of the screen
    if player.ycor() > 280:
        player.start_pos()
        current_score.increase_level()
    # increment the counter once one iteration is completed.
    generate += 1
# prevent the screen from exiting
screen.exitonclick()