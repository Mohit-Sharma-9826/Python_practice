import time
from turtle import Screen
from player import Player
from car_manager import *
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

pl = Player()
cars = CarManager()
level = Scoreboard()

screen.onkeypress(pl.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(level.move_time)
    screen.update()
    cars.move()
    if pl.ycor() == 290:
        pl.reseter()
        level.update()
        level.time_update()

    for i in range(SIZE):
        if pl.distance(cars.cars_grp[i]) < 20:
            game_is_on = False

Over = Turtle()
Over.penup()
Over.hideturtle()
Over.color("red")
Over.write("Game Over!", False, align="center", font=("Courier", 20, "normal"))
    
screen.exitonclick()
