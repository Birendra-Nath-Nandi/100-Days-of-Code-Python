# Control Flow with if / else and Conditional Operators

# Example - Rollercoaster program
print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm?\n> "))

if height >= 120:
    print("You can ride the rollercoaster!")   
else:
    print("Sorry, you have to grow taller before you can ride.")

# Nested if / elif / else

print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm?\n> "))

# Given that height requirement is 120cm
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n> "))
    if age < 12:
        print("Please pay $7.")
    elif age <= 18: # elif statement
        print("Please pay $12.")
    else:
        print("Please pay $18.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Multiple if statement

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n> "))
    if age < 12:
        print("Child tickets $7.")
        bill += 7
    elif age <= 18:
        print("Youth tickets $12.")
        bill += 12
    else:
        print("Adult tickets $18.")
        bill += 18
    wants_photo = input("Do you want a photo taken? Y or N.\n> ")
    if wants_photo == "Y":
        print("Here you go!")
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Logical Operators

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n> "))
    if age < 12:
        print("Child tickets $7.")
        bill += 7
    elif age > 12 and age <= 18:
        print("Youth tickets $12.")
        bill += 12
    elif age >= 45 and age <= 55: # midlife crisis ;D
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets $18.")
        bill += 18
    wants_photo = input("Do you want a photo taken? Y or N.\n> ")
    if wants_photo == "Y" and age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free Photo too!")
    elif wants_photo == "Y":
        print("Here you go!")
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Day 03 Boss Challenge : Treasure Island Game

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
left_or_right = input()
left_or_right = left_or_right.lower()
if left_or_right == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat.")
    wait_or_swim = input()
    wait_or_swim = wait_or_swim.lower()
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        door = input("Which colour do you choose? Type 'red', 'yellow' or 'blue'")
        door = door.lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("It's a room full of beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")