# Day 4 Lessons and Project
# Randomisation and Python Lists
import random
# Generating random integer values between two specified values, both inclusive
# random_int = random.randint(1,50)
# print(f"Integer value: {random_int}")
#
# # Generating random float values
# random_float = "{:.1f}".format(random.random() * 5)
# print(f"Floating value:{random_float}")


# Heads or Tails Exercise 1
# coin_face = random.randint(0,1)
# # toss = "Heads" if coin_face == 0 else "Tails"
# # print(toss)
# if coin_face == 0:
#     print("Tails")
# else:
#     print(f"Heads")

# Python Lists
# states_of_america = [
# "Delaware","Pennsylvania", "New Jersey", "Georgia", "Connecticut",
# "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
# "Virginia", "New York", "North Carolina", "Rhode Island",
# "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
# "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
# "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
# "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
# "West Virginia", "Nevada", "Nebraska", "Colorado",
# "North Dakota", "South Dakota", "Montana", "Washington",
# "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
# "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america[49])
#
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",
#                "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes"]

# Exercise 2 (The Banker Roulette - Who will pay the bill?)
# attendees = input("Please give me the names of the attendees, "
#                   "separated by"
#                   "commas.Vielen Dank!\n")
# attendees_list = attendees.split(", ");
# list_len = len(attendees_list)
# random_attendee = random.randint(0,list_len - 1)
# print(f"{attendees_list[random_attendee]} is going to buy the meal today!")
#


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",
#                "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines",
#           "Apples", "Grapes", "Peaches", "Cherries"]
# veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potates"]

# dirty_dozen = [fruits, veggies]
# print(dirty_dozen)

# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# Exercise 3 Treasure Map
#
# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
#
# map = [row1,row2,row3]
# print(f"{row1}\n {row2}\n {row3}\n")
# position = input("Where do you want to put the treasure?\n")
# column = int(position[0])
# row = int(position[1])
# map[row-1][column -1] = 'X'
# print(f"{row1}\n {row2}\n {row3}\n")

# The Day's Project Rock Paper Scissors
print("Welcome to the 'ROCK💎 ,PAPER📃 ,SCISSORS✂' game. Have Fun!".upper())
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
rock_paper_scissors = [rock, paper, scissors]
user_choice = int(input("Please make a choice.Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.You lose!")
else:
    print(f"{rock_paper_scissors[user_choice]}\n")
    computer_choice = random.randint(0, 2)
    if user_choice == computer_choice:
      print( f"Computer chose: {rock_paper_scissors[computer_choice]}\n It's a draw!")
    elif (user_choice == 0) and (computer_choice == 1):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou lose!")
    elif (user_choice == 1) and (computer_choice == 0):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou win!")
    elif (user_choice == 0) and (computer_choice == 2):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou win!")
    elif (user_choice == 2 ) and (computer_choice == 0):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou lose!")
    elif (user_choice == 1) and (computer_choice == 2):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou lose!")
    elif (user_choice == 2) and (computer_choice == 1):
      print(f"Computer chose: {rock_paper_scissors[computer_choice]}\nYou win!")
