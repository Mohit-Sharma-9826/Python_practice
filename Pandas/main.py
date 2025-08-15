# import csv

# with open("./Pandas/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))

#     print(temperatures)


# https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion
import pandas

data = pandas.read_csv("./Pandas/weather_data.csv")
# # print(data)
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# # l = data["temp"].to_list()
# # avg = sum(l)/len(l)
# # print(avg)

# #data["temp"] is same as data.temp

# print(data.temp.mean())

#Specific Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


dic = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

#Writing or creating
data2 = pandas.DataFrame(dic)
data2.to_csv("./Pandas/new.csv")