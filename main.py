from turtle import Screen
from pillow import Pillow
from squares import Squares
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=450, height=600)
screen.title("falling blocks")
screen.tracer(0)

pillow = Pillow()
squares = Squares()
circles = Squares()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pillow.move_right, "Left")
screen.onkey(pillow.move_left, "Right")

game_is_on = True
num_loop = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # create squares
    if num_loop % 50 == 0:
        squares.create_square("square")

    if num_loop % 120 == 0 and num_loop > 150:
        circles.create_square("circle")
    squares.move_square()
    circles.move_square()

    # detect collision with pillow
    for square in squares.all_squares:
        if square.distance(pillow) < 20:
            square.reset()
            square.penup()
            square.hideturtle()
            square.clear()
            scoreboard.num_score()

    # detect collision with circle
    for circle in circles.all_squares:
        if circle.distance(pillow) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect collision with wall
    for square in squares.all_squares:
        if square.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

    num_loop += 1













screen.exitonclick()