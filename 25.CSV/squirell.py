import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = data['Primary Fur Color']
tot_colors = (set(gray.tolist()))

color_counts =  data['Primary Fur Color'].value_counts().to_csv('exam.csv')
print(color_counts)