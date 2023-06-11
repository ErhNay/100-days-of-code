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
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")