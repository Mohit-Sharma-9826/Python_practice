from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setx(STARTING_POSITION[0])
        self.sety(STARTING_POSITION[1])
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def reseter(self):
        self.setpos(STARTING_POSITION)


