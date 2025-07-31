from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreCount = 0

        with open("./Turtle_Challenges/Snake_game/high_score.txt", "r") as score_file:
            data = score_file.read()
            data_list = data.split(" ")
            self.highScore = int(data_list[-1][0])

        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.scoreCount} High Score: {self.highScore}", False, align="center", font=('Arial', 18, 'normal'))

    def update(self):
        if self.scoreCount > self.highScore:
            self.highScore = self.scoreCount

            with open("./Turtle_Challenges/Snake_game/high_score.txt", "w") as score_file:
                score_file.write(f"The High Score is {self.highScore}")
                
        self.scoreCount = 0
        self.show_score()
    
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
        self.write(f"Score: {self.scoreCount} High Score: {self.highScore}", False, align="center", font=('Arial', 18, 'normal'))