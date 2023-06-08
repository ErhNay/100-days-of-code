# THE HANGMAN PROJECT
# Step 1
import random
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel"]
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Please guess a letter: ").lower()
print(f"You chose: {guess}")
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# //Alternative
# for i in range(0, len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("Right")
#     else:
#         print("Wrong")
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
