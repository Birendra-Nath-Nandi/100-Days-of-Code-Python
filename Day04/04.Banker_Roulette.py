# write a program that will select a random name from a list of names.
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

import random

# Total number of items in list.
list_index = len(names)

# Generate random number between 0 and the last index.
index = random.randint(0, list_index - 1)

# The Chosen One :D
print(f"{names[index]} is going to buy the meal today!")