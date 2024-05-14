# A program That takes a list of Scores & prints out the Highest score

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")