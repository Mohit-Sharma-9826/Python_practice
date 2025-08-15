import pandas

data = pandas.read_csv("./Pandas/squirrel.csv")

gray, red, black = 0, 0, 0
colors = data["Primary Fur Color"].tolist()

for i in colors:
    if i == "Gray":
        gray +=1
    elif i == "Cinnamon":
        red += 1
    elif i == "Black":
        black += 1


dic = {
    "fur color count": ["Gray", "Red", "Black"],
    "count": [gray, red, black]
}

info = pandas.DataFrame(dic)
info.to_csv("./Pandas/new_squirrel.csv")