# Day 9's Lessons, exercises and Project
# Dictionary, Nesting and Secret Auction


# # First Python Dictionary
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "An action done repeatedly",
#     True: "True",
#     123: "This is a number"
# }

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
# scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 100,
# }
#
# # An Empty Dictionary
# student_grades = {}
#
# # Add Grade Interpretation
# for student in scores:
#     score = scores[student]
#     # Simplify Chained Comparison
#     if 91 <= score <= 100:
#         student_grades[student] = "Outstanding"
#     elif 81 <= score <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= score <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)

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

# ****************** NESTING ************************
# capitals = {
#     "Spain": "Madrid",
#     "Norway": "Oslo",
#     "Finland": "Helsinki"
# }

# Nesting a list in a dictionary
# travel_log = {
#     "Spain": ["Madrid", "Malaga", "Gijon"],
#     "Norway": ["Oslo", "Molde", "Stavanger"],
#     "Finland": ["Helsinki", "Vyborg", "Turku"],
# }

# Nesting a dictionary in a dictionary
# travel_log = {
#     "Spain": {"cities_visited": ["Madrid", "Malaga", "Gijon"], "total_visits": 12},
#     "Norway": {"cities_visited": ["Oslo", "Molde", "Stavanger"], "total_visits": 15},
#     "Finland": {"cities_visited": ["Helsinki", "Vyborg", "Turku"], "total_visits": 8},
# }

# Nesting a dictionary in a list

# travel_log = [
#     {
#         "country": "Spain",
#         "cities_visited": ["Madrid", "Malaga", "Gijon"],
#         "total_visits": 12
#
#     },
#     {
#         "country": "Norway",
#         "cities_visited": ["Oslo", "Molde", "Stavanger"],
#         "total_visits": 15
#     },
#     {
#         "country": "Finland",
#         "cities_visited": ["Helsinki", "Vyborg", "Gijon"],
#         "total_visits": 8
#     }
# ]
#
# for tl in travel_log:
#     for log in tl:
#         print(f"{log}: {tl[log]}")

# Exercise 2 Dictionary in List

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]


# def add_new_country(country, visits, cities_visited):
#     #     new_country = {}
#     #     new_country["country"] = country
#     #     new_country["visits"] = visits
#     #     new_country["cities"] = cities_visited
#     #     travel_log.append(new_country)
#     travel_log.append({
#         "country": country,
#         "visits": visits,
#         "cities": cities_visited
#     })
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# # print(travel_log)
# # for log in travel_log:
# #     print(log)
#
# new_travel_log = travel_log
# print(new_travel_log)
# new_travel_log.append({
#     "country": "Ghana",
#     "visits": 45,
#     "cities": ["Accra", "Kumasi", "Cape Coast"]})
# print(new_travel_log)


# The Days Project Blind - Auction
# *********************** SECRET AUCTION ******************************
# Run this code in replit, to leverage replit's clear() function
from blind_auction_art import logo

# from replit import clear
print(logo)
auction_bidders = {}
continue_auction = True


def highest_bidder(auction):
    highest_value = 0
    highest_bidder = ""
    for bidder in auction:
        bid_amount = auction[bidder]
        if bid_amount > 0:
            highest_value = bid_amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder}, with a bid of ${highest_value}.")


while continue_auction:
    name = input("Please enter your name: ")
    price = int(input("What is your bid price: $"))


    # Populate the auction dictionary

    def bidder_info(bidder_name, bid_price):
        # auction[bidder_name] = bid_price
        auction_bidders.update({bidder_name: bid_price})


    bidder_info(name, price)
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if another_bidder == 'yes':
        print("Screen Cleared")
    #     clear()
    else:
        continue_auction = False
        highest_bidder(auction_bidders)
