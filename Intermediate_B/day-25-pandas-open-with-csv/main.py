import os
import csv
import pandas


# Get the absolute path to the directory containing the script.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "weather_data.csv")

# Without pandas.
weather = []
temperatures = []

with open(file_path) as data:
    content = csv.reader(data)

    for line in content:
        weather.append(line)

for day in weather:
    if day[1] == 'temp':
        continue
    temperatures.append(int(day[1]))

# Using pandas.
data = pandas.read_csv(file_path)
print(data[data.temp == data.temp.max()])

data_dict = {
    "students": ["Angela", "James"],
    "scores": [99, 80],
}

data = pandas.DataFrame(data_dict)
print(data)
# data.to_csv("new_data.csv")
