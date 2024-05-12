# Data Types

# 1. String

print("Hello World")
print('Hello World')

# String Concatenation
print("Hello" + "World")
print("Hello" + " " + "World")

# [0] Represents 'H', [1] 'e' and so on...
print("Hello[0]")
print("Hello[3]")

# Can't sum using Strings
print("123" + "342")

# 2. Integer

print(123 + 342)

# To visualize we use commas in between large numbers Like 13,246,421 but in Python we use '_' Underscores Like 13_246_421 so the Compiler assumes 13246421.
print(14_546_423 + 2_353_567)

# 3. Float

print(3.14 - 2.71)
print(23.546 + 3.14159)
# Floats are used to represent real numbers with a fractional part, such as 3.14 or -0.01.

# 4. Boolean

# in True, 'T' must be capital
print(True) # Without Doublequote
# in False, 'F' must be capital
print(False) # Without Doublequote

# Errors :

# "TypeError" : Print function cannot concatenate string and integer datatype
# print(1 + "2")

# "TypeError" : len function can't process int datatype
# len(2354)

# Type Checking

# Type function is used to check the data type
print(type("Hello")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(23.546)) # <class 'float'>
print(type(True)) # <class 'bool'>

# Type Casting

# Typecasting is performed to change a datatype to another
print(str(123)) # 123 --> String
print(int("123")) # 123 --> Integer
print(str(23.546)) # 23.546 --> String
print(float("23.546")) # 23.546 --> Float

# Mathematical Operations

# Addition
print(23 + 4) # Prints 27
# Subtraction
print(144 - 56) # Prints 88
# Multiplication
print(34 * 2) # Prints 68
# Division
print(463 / 22) # Prints 21.045454545454547
# Floor Division
print(234 // 35) # Prints 6
# Modulus
print(345 % 45) # Prints 30
# Exponents
print(3 ** 5) # Prints 243

# These operations follow a priority rule: 

# 1. Parenthesis
# 2. Exponents
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition, Subtraction
# Note : Calculation goes From Left to Right if Operations have same priority level.

# Example:
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
print(3 * 3 + 3 / 3 - 3) #7

# Round Function:

# Without Round Function:
print(3.14159) # 3.14159
print(8 / 3) # 2.6666666666666665

# With Round Function:
print(round(3.14159)) # 3
print(round(3.14159, 1)) # 3.1
print(round(8 / 3)) # 3
print(round(8 / 3, 2)) # 2.67

# F-strings:

name = "John"
age = 23

print(f"Hello {name}. You are {age} years old.")
# Output : Hello John. You are 23 years old.

# Short hand operations:

score = 0 # Initial

# User scores a point
score += 1 # score = score + 1
# User loses a point
score -= 1 # score = score - 1
# User gains 2x points
score *= 2 # score = score * 2
# Half points penalty
score /= 2 # score = score / 2

# print("User's Score is " + score)
# Here we can use F strings
print(f"User's Score is {score}")

# Day 02 Boss Challenge : Tip Calculator.

# Get the total bill amount from the user
print("Welcome to the tip calculator!\n")
# Get the total bill amount from the user
total_bill = int(input("What was the total bill?\n> $"))
# Get the tip percentage from the user
tip = int(input("What percentage tip would you like to give?\n> 10, 12, or 15? > "))
# Get the number of people to split the bill between
people = int(input("How many people to split the bill?\n> "))
# Calculations
total_bill = total_bill + (total_bill * (tip/100))
bill_for_each_person = total_bill / people
# Print the amount each person should pay, rounded to two decimal places
print(f"\nEach person should pay: ${round(bill_for_each_person, 2)}")