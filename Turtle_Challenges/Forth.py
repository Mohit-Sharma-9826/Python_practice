from turtle import *
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

inp = int(input("Width of gap between circles: "))

tim = Turtle()
colormode(255)
screen = Screen()

tim.speed("fastest")
def drawing(num):
    for i in range(360//num):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(num)

drawing(inp)

screen.screensize(500, 500)
screen.bgcolor("skyblue")
screen.exitonclick()