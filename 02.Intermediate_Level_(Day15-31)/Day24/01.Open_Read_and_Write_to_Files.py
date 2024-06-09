# Open the file in read mode using the traditional method
file = open("my_file.txt")

# Read the contents of the file
contents = file.read()

# Print the contents to the console
print(contents)

# Close the file
file.close()

# Using 'with' keyword to open the file and append new text
with open("my_file.txt", mode='a') as file:
    file.write("\nNew Text.")

# Reading the file again to check if the new text was added
with open("my_file.txt", mode='r') as file:
    updated_contents = file.read()

# Print the updated contents to the console
print(updated_contents)