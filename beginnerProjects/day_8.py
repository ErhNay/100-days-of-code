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
# import math
#
#
# def paint_calc(height, width, cover):
#     area = height * width
#     number_of_cans = math.ceil(area / cover)
#     print(f"You'll need {number_of_cans} cans of paint")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 2 Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             print(i)
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Prroject of the day  (Caesar Cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    alphabet.extend(alphabet)
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        shift_amount = 5
    print(f"The {cipher_direction}d text is {end_text}")

#  if cipher_direction == "decode": shift_amount *= -1 can be placed above the for in loop

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
