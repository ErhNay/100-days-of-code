# Day 9's Lessons, exercises and Project
# Dictionary, Nesting and Secret Auction

# First Python Dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "An action done repeatedly",
    True: "True",
    123: "This is a number"
}

# *************Retrieving an item from a Dictionary****************
# print(programming_dictionary["Bug"])
# print(programming_dictionary[True])
# print(programming_dictionary[123])
#
# **************Adding an item to a list*********************
# programming_dictionary["OOP"] = "This is an acronym for Object-Oriented Programming"
# print(programming_dictionary)
#
# ***********Creating an empty dictionary******************
# empty_dictionary = {}
# print(f"An empty dictionary , {empty_dictionary}")
#
# **************Wiping / Deleting an existing Dictionary************
# # print(f"Before wiping: \n {programming_dictionary}")
# # programming_dictionary = {}
# # print(f"After wiping: {programming_dictionary}")
#
# ************Editing an Item in a Dictionary****************
# programming_dictionary["Bug"] = "It means a moth, originally"
# print(programming_dictionary)
# ************The number of items in a Dictionary***************
# print(len(programming_dictionary))
# *********Looping through a list **************
# for student in programming_dictionary:
#     print(f"{student} : {programming_dictionary[student]}")

#   Exercise 1 -  The Grading Program
scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 100,
}

# An Empty Dictionary
student_grades = {}

# Add Grade Interpretation
for student in scores:
    score = scores[student]
    # Simplify Chained Comparison
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)

# Gives the same results as the above
# for student in scores:
#     score = scores[student]
#     if score >= 91 and score <= 100:
#        student_grades[student] = "Outstanding"
#     elif score >= 81 and score <= 90:
#         student_grades[student] = "Exceeds Expectation"
#     elif score >= 71 and score <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
