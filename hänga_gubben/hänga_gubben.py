import random
import os
from ord import words  # Importing a bunch of words that are saved in another python file
import string  # Importing the string library to use the alphabet

# This function randomizes a word out of the words list
def word_generator(words: list) -> str:
    word = random.choice(words)
    # Loops until we get a word without a '-'
    while '-' in word:
        word = random.choice(words)
    return word.upper()  # Returns the word in uppercase

# This function asks the user if they want to play again
def play_again():
    user_choice = input('Do you want to play again? (Y/N)').upper()
    if user_choice == 'Y':
        hang_man()   
    else:
        print('Goodbye!')

# This function contains the main logic for the Hangman game
def hang_man():
    os.system('cls')  # Clears the terminal
    word = word_generator(words)  # Calls the function to get a random word
    word_letters = set(word)  # Creates a set with all unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Creates a set with the entire alphabet
    used_letters = []  # Empty set to keep track of the user's guesses

    life = 10  # Number of lives/attempts

    # Looping as long as there are letters left to guess and lives > 0
    while len(word_letters) > 0 and life > 0:
        print(f'\nThese are the letters you have used:\n{used_letters}\n')  # These lines show the player their guesses and remaining lives
        print(f'You have {life} attempts left')

        # Shows the current state of the word, with '-' for each unknown letter
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f'The word is: {" ".join(word_list)}\n')

        # Takes a guess from the user
        user_guess = input('Guess a letter:\n->  ').upper()

        # Checking if the guessed letter is in the alphabet and hasn't been guessed before
        if user_guess in alphabet - set(used_letters):
            used_letters.append(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print('')
            else:
                life = life - 1  # Deducting a life for incorrect guesses
                print(f'\nYour guess, {user_guess} was not in the word.\n')

        # Informing the user if they've already guessed that letter
        elif user_guess in used_letters:
            print('You have already guessed on that letter.\nTry again.')
        else:
            print('Incorrect input:')  # Handles input that is not a valid character

    # Checking if all lives are lost or the word is completed
    if life == 0:
        print(f'Too bad, you died.\nThe word was: {word}')
        play_again()
    else:
        print(f'CONGRATULATIONS, you got it..\nThe word was indeed: {word}')
        play_again()

# Starts the game
hang_man()