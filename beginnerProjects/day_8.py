# Day Lessons and Project
# Functions with Inputs
# Parameters and Arguments

# Function definitions
# def greet():
#     print("Hello")
#     print("Norbert")
#     print("Welcome back from abroad")
# greet()


# Function with input
# def say_name(name):
#     print(f"Hello, {name}")
#     print(f"Wie geht's, {name}")
#     print("Sprechen sie Deutsch, Herr Norbert")
# say_name('Norbert')

# # Function with Multiple Inputs
# def greet_with(name, location):
#     print(f"Hallo, Herr {name}")
#     print(f"Wie ist es in {location}")


# Positional Arguments
# greet_with('Norbert', 'Russia')
# keyword Arguments
# greet_with(name="Norbert", location="Russia")
# greet_with(location="Russia", name="Norbert")



# Exercise 1 Paint Area Calculator
import math


def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
