# Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}

# dictionary comprehension
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)