from turtle import Turtle
FONTS = ("Courier", 24, "normal")
# Alignment of the scoreboard on the screen
ALIGNMENT = "center"
# Color of the scoreboard
SCORE_COLOR = "White"


class Scoreboard:
    """Scoreboard class that inherits the Turtle class
        The class is responsible for displaying the Score"""

    def __init__(self):
        # start the score at 0
        self.scores = Turtle()
        self.score = 0
        # lift up the pen so it wont draw
        self.scores.penup()
        # set the color to white
        self.scores.color(SCORE_COLOR)
        # set the position to the top of the screen
        self.scores.setposition(0, 270)
        # hide the turtle as we want to display only the score
        self.scores.hideturtle()
        # update function call
        self.update()

    def update(self):
        """this function is responsible for printing the score
        and aligning and font"""
        self.scores.write(f"Score: {self.score}", align=ALIGNMENT, font=FONTS)

    def game_over(self):
        """Game over function which is called when the user crashes into the wall
        or becomes to long and crashes into itself."""
        # set the position to the top of the screen
        self.scores.setposition(0, 0)
        self.scores.write("Game Over", align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.score += 1
        self.scores.clear()
        self.update()
