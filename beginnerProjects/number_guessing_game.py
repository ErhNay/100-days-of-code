from day_12 import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def random_num_generator():
    random_int = random.randint(1, 101)
    return random_int


def difficulty(attempt):
    guess_equal_rand = False
    while not guess_equal_rand:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            guess_equal_rand = True
            return f"You got it!😉😉 The answer was {random_number}"
        else:
            attempt -= 1
            guess_hint = "Too low👇" if guess < random_number else "Too High👆"
            if attempt == 0:
                guess_equal_rand = True
                print(guess_hint)
                return f"You've run out of guesses, you lose😛😋"
            else:
                print(f"{guess_hint}\nGuess again.")


while input("Do you want to play the Number Guessing Game? Type 'y' or 'n': ") == 'y':
    random_number = random_num_generator()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100, guess that number😉")
    print(f"Psst, the correct answer is {random_number}")
    difficulty_level = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        print(difficulty(attempt=EASY_LEVEL))
    else:
        print(difficulty(attempt=HARD_LEVEL))
