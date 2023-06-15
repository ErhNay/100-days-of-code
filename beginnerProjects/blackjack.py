# Day 11 - Capstone Project BlackJack - 21

# ############## Blackjack Project #####################
# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################
from blackjack_art import logo
import random


def deal_card():
    """Returns a random card from a deal card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the score"""
    """Returns the sum of numbers in a list"""
    ace = 11
    score = sum(cards)
    # ace in cards and 10 in cards and len(cards) == 2
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if ace in cards and score > 21:
        cards.remove(ace)
        cards.append(1)
    return score


# Compare scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw😉"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack 👌"
    elif user_score > 21:
        return "You went over. You lose😢"
    elif computer_score > 21:
        return "Opponent went over. You win💃"
    elif user_score > computer_score:
        return "You win🤗😚"
    else:
        return "You lose😜"

# Play game
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score {user_score}")
    print(f"  Your final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()

