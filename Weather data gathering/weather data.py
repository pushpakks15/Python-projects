# # with open("C:/Users/Admin/PycharmProjects/csv/weather_data.csv") as file:
# #     data=file.readlines()
# #     print(data)
# # import csv
# #
# # with open("C:/Users/Admin/PycharmProjects/csv/weather_data.csv") as file:
# #     data=csv.reader(file)
# #     temperatures=[]
# #     for row in data:
# #         temp=row[1]
# #         if row[1] !="temp":
# #             temperatures.append(int(temp))
# #     print(temperatures)
#
import pandas
# data=pandas.read_csv("C:/Users/Admin/PycharmProjects/csv/weather_data.csv")
# # print(data)
#
# # list=temp.to_list()
# # # print(list)
# # # print(sum(list))
# # count=0
# # for number in list:
# #     count+=1
# # print(sum(list)/count)
#
# # average=temp.mean()
# # print(average)
# # print(temp.max())
#
#
# monday=data[data.day=="Monday"]
# # print(monday)
# t=monday.temp
# print((t*(9/5))+32)

data=pandas.read_csv("C:/Users/Admin/PycharmProjects/csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color=data["Primary Fur Color"]
final=color.value_counts()
dict=final.to_dict()
dict2={"Primary Fur color":dict.keys(),"Count":dict.values()}
frame=pandas.DataFrame(dict2)
frame.to_csv("count.csv")








