# Day 10's Lessons and  Project
# Function with output and multiple return values
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't enter valid input!"
#     return f"{f_name.title()} {l_name.title()}"
#
#
# first_name = input("First Name: ")
# last_name = input("Last Name: ")
# output = format_name(first_name, last_name)
# print(output)

# ****************** Exercise 1 DAYS IN MONTH ************************
# def is_leap(year):
#     """Returns True if a given year is a leap year or False if otherwise """
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(a_year, a_month):
#     """Returns the number days in a given month"""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if a_month > len(month_days):
#         return "Please enter a valid number!"
#     if is_leap(a_year) and a_month-1 == 1:
#         return 29
#     return month_days[a_month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# **********************The Calculator Project*********************
# Add
from calculator_logo import logo


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    calculate = True
    while calculate:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new  calculation.: ") == 'y':
            num1 = answer
        else:
            calculate = False
            calculator()


calculator()
