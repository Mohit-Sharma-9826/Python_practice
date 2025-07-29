from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("red")
        self.setpos(-280, 260)
        self.write(f"Level: {self.level}", False, font=FONT)
        self.move_time = 0.005
    
    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, font=FONT)
        
    def time_update(self):
        self.move_time *= 0.9
