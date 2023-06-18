# **************************HIGHER OR LOWER GAME**********************************

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
if random_data1 == random_data2:
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
