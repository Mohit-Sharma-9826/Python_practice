from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.left(90)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(x, y)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        if self.ycor() < 250:
            self.forward(15)

    def down(self):
        if self.ycor() > -250:
            self.backward(15)