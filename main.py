# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data['day'] == 'Monday'])
# print(data[data.day == "Monday"])
# Get the row that has max temperature
# print(data[data.temp == data.temp.max()])

#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Anu"],
    "scores" :  [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
