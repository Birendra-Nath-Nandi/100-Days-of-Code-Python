# file1.txt and file2.txt, each contain a bunch of numbers. create a list called result which contains the numbers that are common in both files.

with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]

print(result)