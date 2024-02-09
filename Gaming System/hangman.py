# Hangman game

import random 

def play_hangman():   
    """
    Allows a player to play the game of Hangman by guessing letters to
    reveal a hidden word, with a limited number of incorrect guesses allowed.
    """
    # List of words for the game
    words = ['elephant', 'sunshine', 'guitar', 'mountain', 'strawberry']
    computer = random.choice(words)
    word_letters = set(computer)  # Set of unique letters in the chosen word
    guessed_letters = set()
    correct_letters = set()
    errors = 0

    print('\033[36m\nWelcome to Hangman!\033[0m')

    stages = [
        """
           +---+
               |
               |
               |
              ===""",
        """
           +---+
           O   |
               |
               |
              ===""",
        """
           +---+
           O   |
           |   |
               |
              ===""",
        """
           +---+
           O   |
          /|   |
               |
              ===""",
        """
           +---+
           O   |
          /|\  |
               |
              ===""",
        """
           +---+
           O   |
          /|\  |
          /    |
              ===""",
        """
           +---+
           O   |
          /|\  |
          / \  |
              ==="""
    ]
    while True:
        print(f'\033[31m{stages[errors]}\033[0m') # Display the current hangman stage
        
        # Display the word with correctly guessed letters revealed
        for letter in computer:
            if letter in correct_letters:
                print(letter, end=" ")
            else:
                print('\033[31m' + '_' + '\033[0m', end=" ")
        
        print()        
        # Display guessed letters
        print('\n\033[36mGuessed letters:\033[0m ', ", ".join(guessed_letters)) 
        
        # Check if the player has made too many errors (lost)
        if errors == len(stages) - 1:
            print('\nYou lost! The word was:', computer)
            break
        
        # Check if all letters have been correctly guessed (won)
        if word_letters == correct_letters:
            print('\nCongratulations, you won!')
            break
   
        guess = input('\n\033[36mGuess a letter (or press # to exit):\033[0m ').lower()

        # Exit the program
        if guess == '#': 
            print('\nExiting the game. Goodbye!')
            break

        # Check if the input is a letter    
        if guess.isdigit():
            print('\n\033[31mPlease enter a letter.\033[0m')
            continue

        if guess in guessed_letters:
            print('\n\033[31mYou have already guessed that letter. Try again.\033[0m')
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_letters:
            correct_letters.add(guess)
        else:
            errors += 1
        
        

           


        
        



        

    
    







