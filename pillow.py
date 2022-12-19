from turtle import Turtle

# pillow
STARTING_POSITIONS = [(0, -280), (-20, -280), (-40, -280)]
MOVE_DISTANCE = 20


class Pillow(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(0, -280)

    def move_left(self):
        self.forward(10)

    def move_right(self):
        self.backward(10)

