from turtle import *
import paddle_fl
import ball_fl
import scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
colormode(255)
screen.bgcolor(123, 158, 249)
screen.listen()
screen.tracer(0)

pad = paddle_fl.Paddle(350, 0)
pad2 = paddle_fl.Paddle(-350, 0)
ball = ball_fl.Ball()
l_score = scoreboard.Score(-50, 250)
r_score = scoreboard.Score(50, 250)

screen.onkeypress(pad.up, "Up")
screen.onkeypress(pad.down, "Down")
screen.onkeypress(pad2.up, "w")
screen.onkeypress(pad2.down, "s")

line = Turtle()
line.color("white")
line.penup()
line.setpos(0, 300)
line.setheading(270)
line.hideturtle()
while True:
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)
    if line.ycor() < -300:
        break
    
while True:
    time.sleep(ball.movetime)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(pad) < 50 and ball.xcor() > 330) or (ball.distance(pad2) < 50 and ball.xcor() < -330):
        ball.hor_bounce()
    
    if ball.xcor() > 390:
        ball.resetpos()
        l_score.change()
    
    if ball.xcor() < -390:
        ball.resetpos()
        r_score.change()
