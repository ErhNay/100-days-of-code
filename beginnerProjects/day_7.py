# THE HANGMAN PROJECT
import random
import hangman_art
import hangman_words

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = hangman_words.word_list
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
# Get Random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# keep track of lives left
lives = 6

print(hangman_art.logo)
# print(f'Pssst, the solution is {chosen_word}.')
# Append '_' to the empty list
display = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Please guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # check if player is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word. "
              f"You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You win!")
    print(hangman_art.stages[lives])



