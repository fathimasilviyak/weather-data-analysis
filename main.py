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
data_dict = data.to_dict()
print(data_dict)
