# Creating a Function

# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")
  
# Calling a Function

# To call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()

# Arguments

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# ERROR:
# If you try to call the function with 1 or 3 arguments, you will get an error:

# Example

# This function expects 2 arguments, but gets only 1:
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# Keyword Arguments

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")