# # with open("weather_data.csv") as weather_file:
# #     data = weather_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# #Average
# # total_temp = len(temp_list)
# # sum = 0
# # for temp in temp_list:
# #     sum += temp
# # print(round(sum/total_temp))
#
# # average = sum(temp_list)/len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
#
# #Max
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)
#
# #Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)
#
# # create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "james", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
