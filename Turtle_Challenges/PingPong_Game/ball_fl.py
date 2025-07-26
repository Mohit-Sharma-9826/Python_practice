from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 2
        self.y_move = 2
        self.movetime = 0.01

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def hor_bounce(self):
        self.x_move *= -1
        self.movetime *= 0.9
    
    def resetpos(self):
        self.movetime = 0.01
        self.goto(0, 0)
        self.hor_bounce()