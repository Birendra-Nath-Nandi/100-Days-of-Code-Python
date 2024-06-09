# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

# Randomly chooses between zero and one.
toss = random.randint(0, 1)

if toss == 1:
    print("Heads")
else:
    print("Tails")