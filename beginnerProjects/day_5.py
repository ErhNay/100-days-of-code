# Day Lessons and Project  => Python Loops
# For Loops, Range and Code Block
#
# fruits = ["Apples", "Oranges", "Grapes"]
#
# for fruit in fruits:
#     print(fruit)
#

# Exercise 1 Average Student Height
# students_height = input("Please enter the heights of the students\n").split(", ")
# total_height = 0
# num_of_students = 0
# average_height = 0
# for std_height in students_height:
#     total_height += int(std_height)
#     num_of_students += 1
# print(f"The sum of their height is {total_height}\nThe number of items in the list is {num_of_students}")
# average_height = total_height / num_of_students
# print(f"The average height of the students is {round(average_height)}")

# Exercise 2 High Score
#  This program calculates the highest score from a List of scores.

# student_scores = input("Please enter each student's score. Thank you\n").split(",")
# max_score = 0
# min_score = 0
# for score in student_scores:
#     score = int(score)
#     if score > max_score:
#         max_score = score
# print(f"The highest score in the class is: {max_score}\n")

# #for loop with range()
# acc = 0
# for number in range(1, 101):
#     acc += number
# print(acc)

# Exercise 3 Adding even numbers in a certain range of numbers
# even_acc = 0
# for even_numbers in range(2, 101, 2):
#     even_acc += even_numbers
# print(even_acc)

# Exercise 3 FizzBuzz Game
# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         number = "FizzBuzz"
#     elif number % 3 == 0:
#         number = "Fizz"
#     elif number % 5 == 0:
#         number = "Buzz"
#     print(number)

# The Day's Project (Password Generator)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
auto_password = []
password = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for letter in range(1, nr_letters + 1):
    random_letter = random.randint(0, len(letters) - 1)
    auto_password.append(letters[random_letter])

for sym in range(1, nr_symbols + 1):
    random_sym = random.randint(0, len(symbols) - 1)
    auto_password.append(symbols[random_sym])

for num in range(1, nr_numbers + 1):
    random_num = random.randint(0, len(numbers) - 1)
    auto_password.append(numbers[random_num])
# print(auto_password)
random.shuffle(auto_password)
generated_password = password.join(auto_password)
print(f"Your password is: {generated_password}")

# Alternative Code
#Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")
