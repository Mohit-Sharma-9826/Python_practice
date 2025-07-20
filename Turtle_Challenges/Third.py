from turtle import *
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
screen = Screen()

screen.screensize(500, 500)
screen.bgcolor("skyblue")

colormode(255)
tim.pensize(10)
tim.color("orange", "yellow")
tim.speed(0)
ang = [0, 90, 180, 270]
for i in range(100):
    ch = random.choice(ang)
    col = random_color()
    tim.pencolor(col)
    tim.forward(50)
    tim.setheading(ch)

screen.exitonclick()