from turtle import *
import snake_fl
import food_fl
import scoreboard
import time

screen = Screen()
screen.setup(600, 600)
colormode(255)
screen.bgcolor(58, 40, 34)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

score = scoreboard.Score()
snake = snake_fl.Snake()
food = food_fl.Food()

body = snake.turtle_list
screen.update()

screen.onkey(lambda: snake.allow_turn(180), "Left")
screen.onkey(lambda: snake.allow_turn(0), "Right")
screen.onkey(lambda: snake.allow_turn(90), "Up")
screen.onkey(lambda: snake.allow_turn(270), "Down")

while True:
    snake.move()

    screen.update()
    time.sleep(0.1)
    
    obj = body[0]
    if body[0].distance(food) < 15:
        food.update_pos()
        score.scoreCount += 1
        score.show_score()
        snake.grow()


    flag = 0
    for i in range(1, len(body)):
        if body[0].distance(body[i]) < 5:
            flag = 1
            
            
    if flag == 1:
        # score.reason()
        score.update()
        snake.restart()
        # break

    if obj.pos()[0] > 290 or obj.pos()[0] < -290 or obj.pos()[1] > 290 or obj.pos()[1] < -290:
        # score.game_over()
        score.update()
        snake.restart()
        # break

screen.exitonclick()