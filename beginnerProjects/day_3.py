# Day Three Lessons, Exercises and Project
# Control Flow and Logical Operators
# Conditional Statements,Logical Operators, Code Blocks and Scope

#Exercise 1
# height = input("Please enter your height in cm: \n")
# height_as_int = int(height)
# bill = 0
# if height_as_int >= 120:
#     print("You qualify to ride on the rollercoaster☺😉☺☺😉☺")
#     age = int(input("Please enter your age \n"))
#     if age <= 0 :
#         print("No payment needed for babies.")
#     elif age < 12:
#         print("Child ticket are $5.00")
#         bill = 5
#     elif age < 18:
#         print("Youth ticket are $7.00")
#         bill = 7
#     elif  age >= 45 and age <= 55:
#         print("Everything will be okay. Free ride on us.")
#     else:
#         print("Adults tickets are $12.00")
#         bill = 12
#     wants_photo = input("Do you want your photo to be taken? Y or N\n")
#     if wants_photo == 'Y':
#         bill += 3
#     print(f"Your total bill is ${bill}")
# else:
#     print(f"You don't qualify to ride on the rollercoaster. Thank you! Try again some other time.😉")
#

# ----------------------------------------------------------------------------------------------------
# #Exercise 2 ODD or EVEN
# userInput = int(input("Please enter a number to find out whether it's odd or even: \n"))
# if (userInput % 2) == 0:
#     print(f"Indeed! {userInput} is even")
# else:
#     print(f"{userInput} is actually odd 😉🥙💥")

# ----------------------------------------------------------------------------------------------------

# Exercise 3 BMI 2.0
# height = float(input("Please enter your height in m:\n"))
# weight = float(input("Please enter your weight in kg:\n"))
#
# bmi = round(weight / height ** 2)
# print(bmi)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi},you're underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi},you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi},you are slightly over weight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi},you are obesed.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obesed")
# ----------------------------------------------------------------------------------------------------

# Exercise 4 (Leap Year )
# year = int(input("What year do you want to check?\n"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"This year,{year} is indeed a leap year")
#         else:
#             print(f"This year,{year} is not a leap year")
#     else:
#         print(f"This year,{year} is indeed a leap year")
# else:
#     print(f"This year, {year} is not a leap year")
# ----------------------------------------------------------------------------------------------------

# Exercise 5 (Pizza Order Practice)
# print("Welcome to Erhnay Pizza🍕🍕🍕 Deliveries")
# size = input("Please what size of pizza do you want? S, M or L\n")
# add_pepperoni = input("Do you want Pepperoni? Y/N\n")
# extra_cheese = input("Do you want extra cheese? Y/N\n")
# price = 0
# if size == 'S':
#     price += 15
#     if add_pepperoni == 'Y':
#         price += 2
#     if extra_cheese == 'Y':
#         price += 1
#     print(f"Your final bill is: ${price}")
# elif size == 'M':
#     price += 20
#     if add_pepperoni == 'Y':
#         price += 3
#     if extra_cheese == 'Y':
#         price += 1
#     print(f"Your final bill is: ${price}")
# elif size == 'L':
#     price += 25
#     if add_pepperoni == 'Y':
#         price += 3
#     if extra_cheese == 'Y':
#         price += 1
#     print(f"Your final bill is: ${price}")

# #     Alternative code
# if size == "S":
#     price += 15
# elif size == 'M':
#     price += 20
# else:
#     price +=25
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         price += 2
#     else:
#         price += 3
#
# if extra_cheese == 'Y'
#     price +=1
#
# print(f"Your final bill is: ${price}")

# ----------------------------------------------------------------------------------------------------

# # Exercise 6 (Love Calculator)
# print("Welcome the Love💖💖 Calculator!\n")
#
# your_name = input("Please enter your name.\n").lower()
# partner_name = input("Please enter your partner's name\n").lower()
# # Concatenating both names
# both_names = your_name +" " +partner_name
# # checking and adding the occurances of t,r,u and e in both names
# true = both_names.count("t") + both_names.count("r") + both_names.count("u") + both_names.count("e")
# # checking and adding the occurances of l,o,v and e in both names
# love = both_names.count("l") + both_names.count("o") + both_names.count("v") + both_names.count("e")
# # Type casting and concatenation of the variables true and love
# love_score = int(str(true)+ str(love))
#
# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# ----------------------------------------------------------------------------------------------------

# The Day's Project  => Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome the Treasure Island 🏴‍☠️!")
print("Follow the prompt and find the treasure.That's your mission")
direction = input("You're now at a crossroad, in which direction would you love to go towards, right or left?\n").lower()

if direction == 'left':
    take_action = input(
    '''
You are at the bank of the river and the treasure is just across the river. "
In other to cross, you'll have to either wait for a boat or swim across."
Do you want to wait or swim? Type either wait or swim to continue your journey.\n''').lower()

    if take_action == 'wait':
        door_color_choice = input('''
You waited patiently for the boat and now you've safely crossed the river. 
Well done! Now, there are three colorful doors hindering you from becoming
ostentatiously rich. Which will you choose? Red, Yellow or Blue. Remember, every choice bears it's 
own surprise, so choose wisely. 
        \n''').lower()

        if door_color_choice == 'red':
            print("Ooops! Surprise! You just got burnt by fire. Sorry, Game Over ")
        elif door_color_choice == 'yellow':
            print("Yaayyyy💃💃💃💃, excellent choice! You've found all the lost treasures. You've won!")
        elif door_color_choice == 'blue':
            print("Ooops! Surprise! You just got eaten by beasts. Sorry Game Over!")
        else:
            print("You chose a door that doesn't exist! Game Over!")
    else:
        print("You got attacked by a trout, Game Over!!! Sorry!!!")
else:
    print("You have fallen into a hole because you chose a wrong direction. Hence, Game Over!!")
