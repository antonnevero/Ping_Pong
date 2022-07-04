from turtle import Turtle
# POSITION_X_OF_PADDLE = 350
# POSITION_Y_OF_PADDLE = 0
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
MOVE_ONE_LEG = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.shape("square")
        self.color("white")

    def up(self):
        new_y = self.ycor() + MOVE_ONE_LEG
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_ONE_LEG
        self.goto(self.xcor(), new_y)




