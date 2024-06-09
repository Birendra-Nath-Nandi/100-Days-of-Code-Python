# print function
print("Hello World!")

# String concatenation in print function
print("Hello" + " " + "World" + "!")

# Errors :

# "SyntaxError" : It's missing a " at the end
# print("Hello world!)

# "IndentationError" : It's because of the Indent before the print function
#    print("Hello World!")

# Problem 1 :  Print - Nik said "Hello there!" in the console

# Process 1
print('Nik said "Hello there!"')
# Process 2
print("Nik said \"Hello there!\"")

# input function
input("What is your name?" )

# input function in action
print("Hello " + input("What is your name? "))

# input function with variable
name = input("What is your name? ")
print("Hello " + name)

# Problem 2 : Swap the values of the variables
a = input()
b = input()

# Swap
Temp = a
a = b
b = Temp

# Print the result
print(a)
print(b)

# Day 01 Boss Challenge : Band Name Generator.

#1. Create a greeting for your program.
print("Welcome to Band Name Generator.\n")

#2. Ask the user for the city that they grew up in.
city_name = input("What's the name of the city you grew up in?\n> ")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n> ")

#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name
print("\nYour band name could be " + band_name)

#5. Make sure the input cursor shows on a new line: