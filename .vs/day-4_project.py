# Day 4 : Rock Paper Scissors game

import random

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

choices = [rock, paper, scissors]

cpu_choice = random.randint(0, 2)

user_choice = int(
    input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors"))
print(choices[user_choice])

print("CPU choose: \n")
print(choices[cpu_choice])

if(cpu_choice == user_choice):
    print("Its a draw")

if(cpu_choice == 0 and user_choice == 1):
    print("You Win")

if(cpu_choice == 0 and user_choice == 2):
    print("You Lose")

if(cpu_choice == 1 and user_choice == 0):
    print("You Lose")

if(cpu_choice == 1 and user_choice == 2):
    print("You Win")

if(cpu_choice == 2 and user_choice == 0):
    print("You Win")

if(cpu_choice == 2 and user_choice == 1):
    print("You Lose")
