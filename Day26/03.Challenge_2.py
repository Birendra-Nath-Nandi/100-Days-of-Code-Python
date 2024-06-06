# Using list comprehension to filter out the even numbers from a series of numbers.

list_of_strings = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55']

# list comprehension to convert strings to integers
numbers = [int(x) for x in list_of_strings]

# list comprehension to filter on even numbers
result = [num for num in numbers if num%2==0]

print(result)