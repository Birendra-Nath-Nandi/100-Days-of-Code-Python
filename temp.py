# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2

# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3

# else:
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3

# if extra_cheese == "Y":
#         bill += 1

# print(f"Your final bill is: {bill}.")

# print("Welcome to the Rollercoaster")
# height = int(input("What is your height in cm?\n> "))

# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?\n> "))
#     if age < 12:
#         print("Child tickets $7.")
#         bill += 7
#     elif age > 12 and age <= 18:
#         print("Youth tickets $12.")
#         bill += 12
#     elif age >= 45 and age <= 55: # midlife crisis ;D
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         print("Adult tickets $18.")
#         bill += 18
#     wants_photo = input("Do you want a photo taken? Y or N.\n> ")
#     if wants_photo == "Y" and age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free Photo too!")
#     elif wants_photo == "Y":
#         print("Here you go!")
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print("The Love Calculator is calculating your score...")
# name1 = "Angela Yu" # What is your name?
# name2 = "Jack Bauer" # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# combined_name = name1 + name2

# lower_case_name = combined_name.lower()
# t = lower_case_name.count("t")
# r = lower_case_name.count("r")
# u = lower_case_name.count("u")
# e = lower_case_name.count("e")

# true_count = t + r + u + e

# l = lower_case_name.count("l")
# o = lower_case_name.count("o")
# v = lower_case_name.count("v")
# e = lower_case_name.count("e")

# love_count = l + o + v + e

# true_love = int(str(true_count) + str(love_count))

# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif true_love >= 40 and true_love <= 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}.")

# # Day 03 Boss Challenge : Treasure Island Game

# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     '"=.|                  |
# |___________________|__"=._o'"-._        '"=.______________|___________________
#           |                '"=._o'"=._      _'"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
#           |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
#  _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
# |                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
# |___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************''')

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
# left_or_right = input()
# left_or_right = left_or_right.lower()
# if left_or_right == "left":
#     print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat.")
#     wait_or_swim = input()
#     wait_or_swim = wait_or_swim.lower()
#     if wait_or_swim == "wait":
#         print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
#         door = input("Which colour do you choose? Type 'red', 'yellow' or 'blue'")
#         door = door.lower()
#         if door == "red":
#             print("It's a room full of fire. Game Over.")
#         elif door == "yellow":
#             print("You found the treasure! You Win!")
#         else:
#             print("It's a room full of beasts. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")

# # List of fruits from the dirty dozen list
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Pears", "Cherries", "Tomatoes"]
# # List of vegetables from the dirty dozen list
# vegetables = ["Spinach", "Kale", "Peppers", "Carrots", "Celery"]

# # Nested lists
# dirty_dozen2 = [fruits, vegetables]

# print(dirty_dozen2)
