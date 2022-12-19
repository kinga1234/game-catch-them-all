from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class Squares:

    def __init__(self):
        self.all_squares = []
        self.square_speed = STARTING_MOVE_DISTANCE
        self.num_loop = 0

    def create_square(self, shape):
        new_square = Turtle(shape)
        new_square.penup()
        new_square.right(90)
        new_square.color(random.choice(COLORS))
        random_x = random.randint(-200, 200)
        new_square.goto(random_x, 300)
        self.all_squares.append(new_square)

    def move_square(self):
        for square in self.all_squares:
            square.forward(self.square_speed)


    # def not_caught(self):
    #     for square in self.all_squares:
    #         if square.ycor() > 280:
    #             return True
    #         else:
    #             return False
