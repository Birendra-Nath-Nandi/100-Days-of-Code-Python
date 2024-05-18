import math

# Function to calculate the number of paint cans required to cover a given wall area
def paint_calc(height, width, cover):
    
    
    number_of_cans = math.ceil((height * width) / coverage)
    
    # Print the number of cans required
    print(f"You'll need {number_of_cans} cans of paint.")


# Get user input for the height and width of the wall
test_h = int(input("Enter the height of the wall (m): ")) # Height of wall (m)
test_w = int(input("Enter the width of the wall (m): ")) # Width of wall (m)

coverage = 5

# Call the paint_calc function with the provided height, width, and coverage
paint_calc(height=test_h, width=test_w, cover=coverage)
