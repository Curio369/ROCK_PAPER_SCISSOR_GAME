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
user_choice = int(input("ENTER A NUMBER : 1 - ROCK ; 2 - PAPER ; 3 SCISSORS : " ))
if user_choice == 1:
    print("YOU CHOSE ROCK", rock)
elif user_choice == 2:
    print("YOU CHOSE PAPER" , paper)
else:
    print("YOU CHOSE SCISSORS" , scissors)

computer_choice = random.randint(1,3)
if computer_choice == 1:
    print("COMPUTER CHOSE ROCK", rock)
elif computer_choice == 2:
    print("COMPUTER CHOSE PAPER" , paper)
else:
    print("COMPUTER CHOSE SCISSORS" , scissors)
if user_choice == 1 and computer_choice == 2:
    print("YOU LOSE AND COMPUTER WON")
elif user_choice == 1 and computer_choice == 3:
    print("YOU WON AND COMPUTER LOST THE GAME")
elif user_choice == 2 and computer_choice == 1:
    print("YOU WON AND COMPUTER LOST THE GAME")
elif user_choice == 2 and computer_choice == 3:
    print("YOU WON AND COMPUTER LOST THE GAME")
elif user_choice == 3 and computer_choice == 1:
    print("YOU LOSE AND COMPUTER WON")
elif user_choice == 3 and computer_choice == 2 :
    print("YOU WON AND COMPUTER LOST THE GAME")
else :
    print("DREW")