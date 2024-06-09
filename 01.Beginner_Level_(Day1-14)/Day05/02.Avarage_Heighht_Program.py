# A program That takes a list of heights and prints out the Total height, number of students & average height.
student_heights = [151, 145, 179] # given

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

# Without using len()
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")