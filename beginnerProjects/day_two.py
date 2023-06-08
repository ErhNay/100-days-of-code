# # Day Two -> Understanding Data Types and String Manipulation
# # Data Types, Numbers, Operations, Type Conversion and f-string
# # There are at least 4 Python Primitive Data Types
# # String
# # data_type1 = "Hello World"
# #
# # # integer
# # data_type2 = 52
# #
# # # float
# # data_type23 = 52.018
# #
# # # boolean
# # valid = True
#
# # Type Error Example
# cast = 1
# num_char = len(input('What is your name?\n'))
# # print('oh, your has '+ num_char + " characters")
# # TypeError: can only concatenate str (not "int") to str
# # Solution
# print('oh, your name has '+ str(num_char) + " characters")
#
# # The type() function checks the type of a value
# print(type(num_char))
#
# # type conversion,
# print(float(num_char))
# print(bool(num_char))
# print(bool(cast))
# print(type(str(num_char)))

# Exercise 1
# two_digit_number = input("Type a two digit number: \n")
#
# num_1 = int(two_digit_number[0])
# num_2 = int(two_digit_number[1])
# print(num_1 + num_2)

# Exercise 2 (BMI Calculator)
# bmi = weight / height * height
# weight = input('Please enter your weight in kg: ')
# height = input('Please enter your height in m: ')
# bmi = int(weight) / float(height)**2
# bmi_as_int = int(bmi)
#
# # using f-string to print the output
# # f-string aids in the mixture of two or more data types
# print(f"Your body mass index (BMI) is {bmi_as_int}")
#
# score = 0
# height_ = 1.8
# isWinning = True
# print(f"Your score is {score},your height is {height_} and you are winning is set to {isWinning} ")

# Life in Weeks Challenge

# age = input("Please enter your current age: ")
# age_as_int = int(age)
# years_left = 90 - age_as_int
#
# days_left =  years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12
#
# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")

# -------------------- The Day's Project (The Tip Calculator) -------------------------
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill:$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = bill + (tip / 100 * bill)
num_to_split_bill = int(input("How many people to split the bill?"))
bill_per_peron = "{:.2f}".format((bill_with_tip / num_to_split_bill))
print(f"Each person should pay: $ {bill_per_peron}")
