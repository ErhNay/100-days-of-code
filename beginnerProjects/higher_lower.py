# **************************HIGHER OR LOWER GAME**********************************


# ****************************MY CODE********************************************
# Import game's arts,data, and choice function
from higherLower_art import logo, vs
from higherLower_data import data
from random import choice


def compare_data(data1, data2):
    """Takes in two sets of data and returns True or False after the comparison
      Also returns an updated version of player's score
    """
    data1_followers = data1["follower_count"]
    data2_followers = data2["follower_count"]
    print(f"Compare A: {format_data(data1)}")
    print(vs)
    print(f"Against B: {format_data(data2)}")

    ans = input("Who has more followers? Type 'A' or 'B': ").upper()
    global score
    if ans == "A" and data1_followers > data2_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        return True
    elif ans == "B" and data2_followers > data1_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        return True
    else:
        score = score
        print(f"Sorry, that's wrong. Final Score: {score}")
        return False


def format_data(acc_data):
    data_name = acc_data['name']
    data_desc = acc_data['description']
    data_country = acc_data['country']
    return f"{data_name}, a {data_desc}, from {data_country}"


# Display Game's Art
print(logo)
score = 0
random_data1 = choice(data)
random_data2 = choice(data)

# Generate new data if both data are equal
while random_data1 == random_data2:
    random_data2 = choice(data)

# Game Repetition
should_compare = False
while not should_compare:
    if compare_data(random_data1, random_data2):
        random_data1.clear()
        random_data1.update(random_data2)
        random_data2 = choice(data)
    else:
        should_compare = True

# ****************************Tutor's CODE********************************************
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear
#
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0A
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()