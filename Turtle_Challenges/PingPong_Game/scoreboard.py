from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setpos(x, y)
        self.write(f"{self.score}", False, font=('Arial', 18, 'normal'))

    def change(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, font=('Arial', 18, 'normal'))
