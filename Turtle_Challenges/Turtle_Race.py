from turtle import *
import random

screen = Screen()
screen.setup(800, 600)
colormode(255)
screen.bgcolor(205, 241, 246)
inp = screen.textinput("Make your bet!", "Which turtle will win the race? Enter turtle color (yellow, green, blue, red, orange): ")

yellow = Turtle()
yellow.penup()
yellow.shape("turtle")
yellow.color("orange", "yellow")
yellow.setpos(-360, 100)
yellow.shapesize(1.5)

green = Turtle()
green.penup()
green.shape("turtle")
green.color("LightGreen", "green")
green.setpos(-360, 50)
green.shapesize(1.5)

blue = Turtle()
blue.penup()
blue.shape("turtle")
blue.color("LightBlue", "blue")
blue.setpos(-360, 0)
blue.shapesize(1.5)

red = Turtle()
red.penup()
red.shape("turtle")
red.color("pink", "red")
red.setpos(-360, -50)
red.shapesize(1.5)

orange = Turtle()
orange.penup()
orange.shape("turtle")
orange.color("orange", "orange")
orange.setpos(-360, -100)
orange.shapesize(1.5)

racers = [yellow, green, blue, red, orange]

line = Turtle()
line.hideturtle()
line.speed("fastest")
line.color("red")
line.pensize(10)
line.penup()
line.setpos(370, 200)
line.pendown()
line.right(90)
line.forward(400)

winner = "nobody"
while True:
    flag = 0
    for racer in racers:
        if(racer.pos()[0] < 350):
            racer.forward(random.randint(1, 20))
        else: 
            winner = racer.color()[1]
            flag = 1
            break
    if flag == 1:
        break

if inp.lower() == winner.lower():
    print(f"You won the bet! {winner.capitalize()} turtle is the winner!")
else:
    print(f"You loose! {winner.capitalize()} turtle is the winner!")


screen.exitonclick()