# Rock, Paper, Scissors game

from random import randint
from time import sleep
import emoji

rock = emoji.emojize(':raised_fist:')
paper = emoji.emojize(':raised_hand:')
scissors = emoji.emojize(':victory_hand:')
itens = ('Rock', 'Paper', 'Scissors')
emojis = (rock, paper, scissors)

def play_game():
    """
    Allows the user to play a game of rock-paper-scissors against the computer.
    """
    done = False
    while not done:

        print('\033[36m\nWelcome to the game!' )
        print('-=' * 25)
        print(f'[0] ROCK {rock}')
        sleep(1)
        print(f'[1] PAPER {paper}')
        sleep(1)
        print(f'[2] SCISSORS {scissors}')
        sleep(1)
        print('-=' * 25 + '\033[0m')

        # Takes input for the player's move, validates it and handles exceptions.
        try:
            player = int(input('What is your move? (0, 1, 2 or 9 to exit): '))
            if not (0<= player <=2) and player != 9:
                print('\nInvalid move.')
                continue
        except ValueError:
            print('\nPlease enter a number.')
            continue

        # Exit the program
        if player == 9: 
            print('\nExiting the game. Goodbye!')
            done = True
            break
        
        # Generates a random move for the computer.
        computer = randint(0,2) 
        
        # Prints the chosen moves of the player and the computer with the emojis.
        print('\033[36m' + '-=' * 25 + '\033[0m')
        print(f'The computer played \033[1;30m{itens[computer]}\033[0m{emojis[computer]}')
        print(f'You played \033[1;30m{itens[player]}\033[0m{emojis[player]}')
        print('\033[36m' + '-=' * 25 + '\033[0m')

        # Compares player and computer moves, prints the result of the round.
        if computer == 0: # Rock
            if player == 0:  # Rock
                print('DRAW')
            elif player == 1: # Paper
                print('YOU WON!')
            elif player == 2: # Scissors
                print('YOU LOST')

        elif computer == 1: # Paper
            if player == 0:  # Rock
                print('YOU LOST')
            elif player == 1: # Paper
                print('DRAW')
            elif player == 2: # Scissors
                print('YOU WON!')

        elif computer == 2: # Scissors
            if player == 0: # Rock
                print('YOU WON!')
            elif player == 1: # Paper
                print('YOU LOST')
            elif player == 2: # Scissors
                print('DRAW')
        
   


 

    





