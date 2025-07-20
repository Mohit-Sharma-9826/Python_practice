from turtle import Turtle, Screen

triangle = Turtle()
triangle.color("red", "orange")
triangle.teleport(-250, 200)
for _ in range(3):
    triangle.forward(100)
    triangle.left(120)

sq = Turtle()
sq.color("green")
sq.teleport(-100, 200)
for _ in range(4):
    sq.forward(100)
    sq.left(90)


pent = Turtle()
pent.color("blue")
pent.teleport(100, 150)
for _ in range(5):
    pent.forward(100)
    pent.left(72)

all_shapes = Turtle()
all_shapes.teleport(0, -150)
col = ["red", "blue", "green", "orange"]
ind = 0
for i in range(3, 10):
    all_shapes.color(col[ind])
    ind = (ind+1)%len(col)
    loc = all_shapes.position()
    all_shapes.teleport(loc[0], loc[1]-15)
    for j in range(i):
        all_shapes.forward(100)
        ang = 180 - (((i-2)*180)/i)
        all_shapes.left(ang)


screen = Screen()
screen.exitonclick()