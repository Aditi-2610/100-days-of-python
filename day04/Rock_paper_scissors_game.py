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
user_choice = int(input("what do you choose? Press 0 for Rock, 1 for Paper, and 2 for Scissors: \n"))
choices = [rock, paper, scissors]
computer_choice = random.randint(0,2)

print("You chose:\n")
print(choices[user_choice])
print("\n Computer chose: \n")
print(choices[computer_choice])


if user_choice == computer_choice:
    print("Its a draw")

elif user_choice > computer_choice:
    print("You win!")

elif user_choice < computer_choice:
    print("You lose!")

else:
    print("You typed an invalid input! Try again.")



