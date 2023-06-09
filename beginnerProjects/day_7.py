# THE HANGMAN PROJECT
# Step 1
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["aardvark", "baboon", "camel", "apple"]
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
# Get Random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# keep track of lives left
lives = 6
print(f'Pssst, the solution is {chosen_word}.')
# Append '_' to the empty list
display = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    # Check guessed letter
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # check if guess is not in chosen word
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])



