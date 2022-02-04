from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.heading()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_pos(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.7
