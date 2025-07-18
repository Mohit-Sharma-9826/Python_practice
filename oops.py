from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "blue")
timmy.pencolor("orange")
timmy.forward(200)
timmy.left(90)
timmy.forward(200)
timmy.begin_fill()
timmy.left(90)
timmy.forward(200)
timmy.home()
timmy.speed(0)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)

my_Screen = Screen()
print(my_Screen.canvheight)
my_Screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Chalizard", "Richu", "Pichu"])
# table.add_column("Type", ["Electric", "Fire", "Electric", "Electric"])
# table.align = "c"  # "l", "c", "r"
# print(table)