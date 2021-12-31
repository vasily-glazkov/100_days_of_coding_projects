import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

stages = hangman_art.stages

chosen_word = random.choice(word_list)

end_of_game = False

lives = 6

guessed_letters = []

print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.\n')

# Creating blanks
display = []
for i in range(0, len(chosen_word)):
    display.append("_")
print(display, '\n')

print(stages[-1])

# Main logic of the game
while not end_of_game:
    
    guess = input('\nEnter a letter: ').lower()

    # Check if letter already guessed
    if guess in display:
        print("You've already checked this letter. Try another.")

    # Check guessed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    print(display)

    # Check if guessed letter not in the word and reduce lives by 1
    if guess not in chosen_word:
        if guess in guessed_letters:
            print("You've already checked this letter. Try another.")
        else:
            print(f"The letter {guess} is not in the word. You have {lives - 1} live(s) left.")
            guessed_letters.append(guess)
            lives -= 1
            print(stages[lives])
            print(display)

    # Check if the user win or loose
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")
    elif lives == 0:
        end_of_game = True
        print(f"\nYou loose. The solution is: {chosen_word}.")
            

print('\n', display)        
