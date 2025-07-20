import colorgram
from turtle import *

# Selecting colors except the white background color from the image.jpg
rgb_colors = []
colors = colorgram.extract('./Turtle_Challenges/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

for i in rgb_colors:
    if i[0]>225 and i[1]>225 and i[2]>225:
        rgb_colors.remove(i)

# Working on the GUI
tim = Turtle()
screen = Screen()
colormode(255)
screen.bgcolor((220, 220, 220))

tim.speed("fastest")
tim.teleport(-220, -220)
tim.hideturtle()
st_loc = tim.position()
y = st_loc[1]
ind = 0
for i in range(10):
    tim.teleport(st_loc[0], y)
    y += 50
    for j in range(10):
        loc = tim.position()
        tim.dot(20, rgb_colors[ind])
        ind = (ind+1)%len(rgb_colors)
        tim.teleport(loc[0]+50, loc[1])

screen.exitonclick()