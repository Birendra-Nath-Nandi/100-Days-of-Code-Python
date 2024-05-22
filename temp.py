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
#         door = input("Which color do you choose? Type 'red', 'yellow' or 'blue'")
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

# Input a Python list of student heights
# student_heights = [151, 145, 179] # Given

# total_hight = 0

# for x in student_heights:
#     total_hight += x

# avg = int(total_hight/len(student_heights))

# print(f"total height = {total_hight}")
# print(f"number of students = {len(student_heights)}")
# print(f"average height = {avg}")

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# max = 0
# for num in student_scores:
#     if num > max:
#         max = num

# print(f"The highest score in the class is: {max}")

# rows = 5 # int(input("How meany rows you want?> "))

# print("\nfront facing star half pyramid")

# # front facing star half pyramid
# for num in range(1, rows + 1):
#     print("* " * num)

# print("\nreverse star half pyramid")

# # reverse star half pyramid
# for num in range(rows, 0, -1):
#     print("* " * num)

# print("\nback facing star half pyramid")

# # back facing star half pyramid
# for num in range(rows, 0, -1):
#     print("  " * (num - 1) + "* " * (rows + 1 - num))

# print("\nback facing reverse star half pyramid")

# # back facing reverse star half pyramid
# for num in range(rows, 0, -1):
#     print("  " * (rows - num) + "* " * num)

# print("\nup facing full pyramid")

# # up facing full pyramid
# for num in range(rows, 0, -1):
#     print("  " * (num - 1) + "* " * (2 *(rows + 1 - num) - 1))

# print("\ndown facing full pyramid")

# down facing full pyramid
# for num in range(rows, 0, -1):
#     print("  " * (rows - num) + "* " * (2 * num - 1))

# print("\nleft side facing pyramid")

# left side facing pyramid

#Step 1 

# word_list = ["aardvark", "baboon", "camel"]

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random

# chosen_word = random.choice(word_list)

# blank_list = []
# display_word = ""

# for blanks in range(len(chosen_word)):
#     blank_list.append("_")
# print(blank_list)

# for word_blanks in blank_list:
#     display_word += "_ "

# print(f"Word : {display_word}")

# # print("\nWord : " + "_ " * len(chosen_word) + "\n")

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# index = 0

# for x in range(len(chosen_word_list)):
#     if guess in chosen_word_list[index]:
#         blank_list[index] = guess
#     index += 1

# guessed = ""

# print(blank_list)
# for letter_guessed in blank_list:
#     guessed += letter_guessed + " "
# word_str = guessed.upper()
# print(f"word : {word_str}")

# import random
# from art import logo

# def game(no_try, ans):
#     for _ in range(no_try):
#         print(f"You have {no_try} attempts remaining to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == ans:
#             print(f"You got it! The answer was {ans}.")
#             break
#         elif guess < ans:
#             print("Too Low")
#         elif guess > ans:
#             print("Too High")
#         print("Guess again.")
#         no_try -= 1
#     print("You've run out of guesses, you lose")


# random_integer = random.randint(1, 100)

# print(logo)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# # Test
# print(f"Pssst, the correct answer is {random_integer}")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# if difficulty == "easy":
#     no_of_try = 10
# else:
#     no_of_try = 5
    
# game(no_of_try, random_integer)
