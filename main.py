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
# for cars in range(CarManager)
# turtle = Turtle()
# turtle.penup()
# turtle.shape("turtle")
# turtle.heading()
# turtle.left(90)
# turtle.goto(0, -280)


# def go_up():
#     turtle.forward(30)

# Car object
# car = Turtle()
# car.penup()
# car.color("White")
# car.shape("square")
# car.shapesize(stretch_wid=2, stretch_len=1)
# car.left(90)
# car.goto(250, 0)

screen.listen()
screen.onkey(player.go_up, "Up")

# # garage = []
# count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_garage.add_car()
    cars_garage.movement()
    # cars.movement()
    # if cars.xcor() < -330:
    #     cars.random_start()
    if player.ycor() > 280:
        player.start_pos()
