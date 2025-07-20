from turtle import *

tully = Turtle()
tully.shape("turtle")
tully.color("red", "orange")
for _ in range(10):
    tully.forward(10)
    tully.penup()
    tully.forward(10)
    tully.pendown()


my_screen =  Screen()
my_screen.exitonclick()
