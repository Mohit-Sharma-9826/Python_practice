from turtle import *

MOVE_DISTANCE = 10
SNAKE_SIZE_SCALE = 0.5
SNAKE_SPEED = "fastest"
SNAKE_COLOR = "white"
SNAKE_BOUNDRY_COLOR = "black"
SNAKE_SHAPE = "square"
SNAKE_BODY_BOXES = 3

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.num = SNAKE_BODY_BOXES
        self.x = (self.num//2)*MOVE_DISTANCE if self.num%2 != 0 else (self.num//2 + (self.num//2 - 1))*(MOVE_DISTANCE/2)
        self.create_snake()
    
    def create_snake(self):
        for _ in range(self.num):
            tim = Turtle()
            tim.penup()
            tim.setpos(self.x, 0)
            self.x -= MOVE_DISTANCE
            tim.color(SNAKE_BOUNDRY_COLOR, SNAKE_COLOR)
            tim.speed(SNAKE_SPEED)
            tim.shape(SNAKE_SHAPE)
            tim.shapesize(SNAKE_SIZE_SCALE)
            self.turtle_list.append(tim)
        
    def grow(self):
        tim = Turtle()
        tim.penup()
        tim.setpos(self.turtle_list[-1].pos())
        tim.color(SNAKE_BOUNDRY_COLOR, SNAKE_COLOR)
        tim.speed(SNAKE_SPEED)
        tim.shape(SNAKE_SHAPE)
        tim.shapesize(SNAKE_SIZE_SCALE)
        self.turtle_list.append(tim)

    def move(self):
        for i in range(len(self.turtle_list)-1,0,-1):
            a = self.turtle_list[i]
            b = self.turtle_list[i-1]
            x = b.pos()[0]
            y = b.pos()[1]
            a.setpos(x,y)

        first = self.turtle_list[0]
        first.forward(MOVE_DISTANCE)

    def allow_turn(self, ch_dir):
        obj = self.turtle_list[0]
        cur_dir = self.turtle_list[0].heading()
        diff = int(abs(cur_dir - ch_dir))
        if diff != 180:
            obj.setheading(ch_dir)

    def restart(self):
        for i in self.turtle_list:
            i.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
