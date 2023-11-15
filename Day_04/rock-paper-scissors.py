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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

game_array = [rock, paper, scissors]

rand_comp_choice = random.randint(0, (len(game_array) - 1))

if user_choice not in [0, 1, 2]:
    print("Invalid input")

elif user_choice == rand_comp_choice:
    print(f"{game_array[user_choice]}\nComputer Chose:\n{game_array[rand_comp_choice]}\nIt's a tie ")

elif (
        (user_choice == 0 and rand_comp_choice == 2) or
        (user_choice == 1 and rand_comp_choice == 0) or
        (user_choice == 2 and rand_comp_choice == 1)
    ):
    print(f"{game_array[user_choice]}\nComputer Chose:\n{game_array[rand_comp_choice]}\nYou won ")

else:
    print(f"{game_array[user_choice]}\nComputer Chose:\n{game_array[rand_comp_choice]}\nComputer won ")
