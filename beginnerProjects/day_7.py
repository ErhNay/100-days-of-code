# THE HANGMAN PROJECT
# Step 1
import random
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel", "apple"]
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_word = random.choice(word_list)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')
# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_
# "representing each letter to guess.
display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append('_')
print(display)
guess = input("Please guess a letter: ").lower()
print(f"You chose: {guess}")
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# //Alternative
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(0, word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    else:
        print("Wrong")
# Print 'display' and you should see the guessed letter in the correct position and every other letter replaced with
# "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

