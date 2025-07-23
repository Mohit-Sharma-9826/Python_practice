from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5)
        self.color("red")
        self.update_pos()
    
    def update_pos(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 260)
        self.goto(rand_x, rand_y)
        
