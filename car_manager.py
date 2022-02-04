from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        # new_car.left(90)
        new_car.goto(320, random.randrange(-250, 250))
        # new_car.x_move = -3
        # new_car.y_move = 0
        # new_car.move_speed = 0.03
        self.all_cars.append(new_car)
        # new_car.random_start()

    def movement(self):
        # self.random_start()
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def random_start(self):
    #     self.new_carcolor(random.choice(COLORS))
    #     self.goto(320, random.randrange(-250, 250))
