from turtle import Turtle

# font for the scoreboard
FONTS = ("Courier", 24, "normal")
# Alignment of the scoreboard on the screen
ALIGNMENT = "center"
# Color of the scoreboard
SCORE_COLOR = "White"


class Scoreboard:
    """Scoreboard class responsible for displaying the Level"""
    def __init__(self):
        # start the score at 0
        self.level_display = Turtle()
        # user level
        self.level = 1
        # lift up the pen so it won't draw
        self.level_display.penup()
        # set the color to white
        self.level_display.color(SCORE_COLOR)
        # set the position to the top of the screen
        self.level_display.setposition(-220, 250)
        # hide the turtle as we want to display only the score
        self.level_display.hideturtle()
        # update function call
        self.update()

    def update(self):
        """this function is responsible for printing the score
        and aligning and font"""
        self.level_display.write(f"Level: {self.level}", align=ALIGNMENT, font=FONTS)

    def game_over(self):
        """Game over function which is called when the user crashes into the wall
        or becomes to long and crashes into itself."""
        # set the position to the top of the screen
        self.level_display.setposition(0, 0)
        self.level_display.write("Game Over", align=ALIGNMENT, font=FONTS)

    def increase_level(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.level += 1
        self.level_display.clear()
        self.update()
