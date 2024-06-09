# Lists

# A list is a collection of items that can be of any data type, including strings, integers, floats, and booleans. Lists are defined using square brackets [] and elements are separated by commas.

my_list = ["item1", 'item2', 23, 34.5, True]
print(my_list) # Output: ["item1", 'item2', 23, 34.5, True]

# Here fruits is a list, stores Name of the fruits in strings
Fruits = ["apple", "banana", "orange"]

print(Fruits[0]) # Output: "apple"
print(Fruits[1]) # Output: "banana"
print(Fruits[2]) # Output: "orange"
# print(Fruits[3]) # Output: IndexError: list index out of range

# Negative indexing
print(Fruits[-1]) # Output: "orange"
print(Fruits[-2]) # Output: "banana"
print(Fruits[-3]) # Output: "apple"

# Lists are mutable, meaning that their elements can be changed after they have been created.

Fruits[0] = "mango"
print(Fruits) # Output: ["mango", "banana", "orange"]

Fruits.append("grape") # add "grape" to the end of the list
print(Fruits) # Output: ["apple", "banana", "orange", "grape"]

Fruits.insert(0, "kiwi") # insert "kiwi" at the beginning of the list
print(Fruits) # Output: ["kiwi", "apple", "banana", "orange", "grape"]

Fruits.remove("banana") # remove "banana" from the list
print(Fruits) # Output: ["kiwi", "apple", "orange", "grape"]

Fruits.pop() # remove the last element from the list
print(Fruits) # Output: ["kiwi", "apple", "orange"]

Fruits.clear() # clear the list
print(Fruits) # Output: []

# List of states in America
states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# print(states_of_america[51]) # Output: IndexError: list index out of range

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Pears", "Cherries", "Tomatoes", "Peppers", "Carrots", "Celery"]

# List of fruits from the dirty dozen list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Pears", "Cherries", "Tomatoes"]
# List of vegetables from the dirty dozen list
vegetables = ["Spinach", "Kale", "Peppers", "Carrots", "Celery"]

# Nested lists
dirty_dozen2 = [fruits, vegetables]

print(dirty_dozen2)