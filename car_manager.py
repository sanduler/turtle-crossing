from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.left(90)
        self.random_start()
        self.x_move = -3
        self.y_move = 0
        self.move_speed = 0.03

    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def random_start(self):
        self.goto(0, random.randrange(-280, 280))
