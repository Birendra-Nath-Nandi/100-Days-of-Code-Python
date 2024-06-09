# Reading CSV Data

with open("CSVs/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    
import csv

# or

with open("CSVs/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
    
# or

import pandas

data = pandas.read_csv("CSVs/weather_data.csv")
print(data['temp'])