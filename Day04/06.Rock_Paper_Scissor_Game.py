# Day 03 Boss Challenge : Rock, Paper & Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

game_images = [rock, paper, scissors]

user_choice = int(input("> "))

if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number, you lose!")
else:
    computer_choice = random.randint(0, 2)
    print(f"You chose {game_images[user_choice]}")
    print(f"Computer chose {game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")