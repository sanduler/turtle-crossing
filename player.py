from turtle import Turtle

# starting position for the turtle
STARTING_POSITION = (0, -280)
# moving distance on click
MOVE_DISTANCE = 10
# determine where the finish line is
FINISH_LINE_Y = 280


class Player(Turtle):
    """This class represents a player it
    inherets all the functionality from the Turtle class"""
    def __init__(self):
        super().__init__()
        # lift up the pen
        self.penup()
        # determine the shape of the player
        self.shape("turtle")
        # set the color
        self.color("white")
        # determine the heading for the player (function)
        self.heading()
        # rotate the turtle
        self.left(90)
        # turtle is set at the start of the game to starting position
        self.goto(STARTING_POSITION)
        # set the initial position for level 1
        self.move_speed = 0.1

    def go_up(self):
        """
        this function is responsible for moving the player up to the goalposition
        the distance rate is preset and can be changed at MOVE_DISTANCE
        """
        self.forward(MOVE_DISTANCE)

    def start_pos(self):
        """start_pos is responsible for bringing back the player to the starting position.
        then increase the speed of the game once the level is increased."""
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.7
