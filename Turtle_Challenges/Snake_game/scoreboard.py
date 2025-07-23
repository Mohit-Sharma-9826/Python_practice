from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreCount = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.scoreCount}", False, align="center", font=('Arial', 18, 'normal'))
    
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over!", False, align="center", font=('Arial', 18, 'normal'))

    def reason(self):
        self.color("red")
        self.goto(0 ,0)
        self.write(f"        Game Over! \n Snake hit its own tail!", False, align="center", font=('Arial', 18, 'normal'))
        
    def show_score(self):
        self.clear()
        self.write(f"Score: {self.scoreCount}", False, align="center", font=('Arial', 18, 'normal'))