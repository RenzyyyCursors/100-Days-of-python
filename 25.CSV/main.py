# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         if i[1].isnumeric():
#             temps = int(i[1])
#             temperatures.append((int(i[1])))
#         else:
#             temps = i[1]

#     print(temperatures)
import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)

# temp_list = data['temp'].tolist()
# print(data.temp.max())

# print(data[data.temp  == data.temp.max()])

# print((data[data.day == 'Monday'].temp)*(9/5)+32)

# Create a dataframe from scratch
data_dict = {'students' : ['amy','james','angela'],
            'scores': [76,56,65]

}

dat2 = pandas.DataFrame(data_dict)
print(dat2)
dat2.to_csv('new dats.csv')