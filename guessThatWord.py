import random
import sys

def choose_word():
    word_list = ["apple", "banana", "cherry", "grape", "orange"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
        display += ' '  # Add a space between letters
    return display.rstrip()  # Remove trailing space

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of allowed incorrect attempts

    print("Welcome to Guess That Word!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)

        guess = raw_input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
            display = display_word(word, guessed_letters)
            print(display)
            if display.replace(' ', '') == word:  # Remove spaces for comparison
                print("Congratulations, you've guessed the word:", word)
                break
        else:
            print("Incorrect!")
            attempts -= 1


    if attempts == 0:
        print("\nSorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
