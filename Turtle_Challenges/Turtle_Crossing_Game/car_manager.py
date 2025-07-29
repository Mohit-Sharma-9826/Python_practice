from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
SIZE = 20

class CarManager:
    def __init__(self):
        self.cars_grp = []
        self.ind = 0
        self.createCars()

    def createCars(self):
        for i in range(SIZE):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.setpos(random.randrange(320, 600, 50), random.randint(-250, 250))
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            for i in range(len(self.cars_grp)):
                if i != 0 and car.distance(self.cars_grp[i]) < 100:
                    car.setx(car.xcor() + 100)

            self.cars_grp.append(car)

    def move(self):
        if self.ind == SIZE:
            self.ind = 0
        else:
            a = self.cars_grp[self.ind]
            a.forward(STARTING_MOVE_DISTANCE)
            self.ind += 1

            if a.xcor() < -320:
                a.setx(random.randrange(320, 500, 10))
                a.sety(random.randint(-250, 250))

