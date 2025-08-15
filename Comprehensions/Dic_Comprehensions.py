marks = {
    "Alex": 90,
    "Liber": 85,
    "Steve": 60,
    "Joginder": 33
}

# dic = {key: value for (key, value) in marks.items() if value > 75}
# print(dic)

import pandas

students = pandas.DataFrame(list(marks.items()), columns=["Name", "Marks"])
print(students)

for (index, rowData) in students.iterrows():
    print(rowData.Name)