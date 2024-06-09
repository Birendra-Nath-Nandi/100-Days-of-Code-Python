# DataFrames & Series: Working with Rows & Columns

import pandas

data = pandas.read_csv("Day25/weather_data.csv")
print(type(data))
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(f"Avg temp = {sum(temp_list)/len(temp_list)}")

# or
print(f"Avg temp = {data['temp'].mean()}")

print(f"Max value = {data['temp'].max()}")
print(f"Min value = {data['temp'].min()}")

# data in Columns
print(data['condition'])
print(data.condition)

# data in Rows
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)

data = {'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
        'Age': [20, 21, 19, 18]}
 
data = pandas.DataFrame(data)
data.to_csv("Day25/New_DataFrame.csv")