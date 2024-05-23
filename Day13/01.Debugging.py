# DEBUGGING

# Describe Problem
def my_function():
# for i in range(1, 20): 
# Generates number between 1 to 19
# Show the i never equals to 20
  for i in range(1, 21): # fix
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# When we are using a list the index starts from 0
# In this bug, the 6 index occasionally causing an issue
dice_num = randint(0, 5) # fix
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
# Theres no condition for 1994
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors
# # There was a typecasting error and a Indentation error
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# Using the print statement, can cheque what part of the code is bugging the programme
# Here the issue is '=='
word_per_page == int(input("Number of words per page: "))
print(f"Pages = {pages}")
print(f"Words/page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)

# Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  # Here the issue is indentation
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])