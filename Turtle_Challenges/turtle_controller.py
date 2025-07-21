from turtle import *

tim = Turtle()
tim.speed("fastest")
screen = Screen()

def move_forward():
    global tim
    tim.forward(10)

def move_backward():
    global tim
    tim.backward(10)

def turn_left():
    global tim
    tim.left(10)

def turn_right():
    global tim
    tim.right(10)

def delete():
    global tim
    tim.reset()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(turn_left, "a")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(delete, "c")
screen.exitonclick()