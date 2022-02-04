from turtle import Turtle
import random
# colors that are generated for the cars. More colors can be added to the list
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "skyblue", "turquoise", "maroon"]
# starting distance for the cars that are going
STARTING_MOVE_DISTANCE = 5
# movement speed
MOVE_INCREMENT = 10


class CarManager:
    """CarManager class is responsible for all the car objects in the main game.
    The constructor initializes the blank list where all the car objects will be stored."""
    def __init__(self):
        self.all_cars = []

    def add_car(self):
        """creates a car in form of the rectangle and sets a random color for it.
        Then the car is appended to the list/"""
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(320, random.randrange(-250, 250))
        self.all_cars.append(new_car)

    def movement(self):
        """Starts the movement of the car on the screen by using a for loop to go through each
        car and move it."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

