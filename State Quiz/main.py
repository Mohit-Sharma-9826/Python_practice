import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./State Quiz/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./State Quiz/50_states.csv")
states = data["state"].tolist()
guessed_states = []
missing_states = states

num = 1
while num <= 50:
    inp = screen.textinput(f"Guessed states({num-1}/50)", "What's another state's name?")
    if inp == "exit":
        dic = {
            "state": missing_states
        }
        new_data = pandas.DataFrame(dic)
        new_data.to_csv("./State Quiz/missingData.csv")
        break
    for i in states:
        if i.lower() == inp.lower() and inp not in guessed_states:
            guessed_states.append(i)
            missing_states.remove(i)
            name = turtle.Turtle()
            name.penup()
            name.hideturtle()
            x = data[data.state == i]["x"].tolist()[0]
            y = data[data.state == i]["y"].tolist()[0]
            name.setpos(x, y)
            name.write(i, False, align="center", font=("Arial", 8, "normal"))
            num += 1


