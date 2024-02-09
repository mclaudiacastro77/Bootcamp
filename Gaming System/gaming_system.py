# Rock, Paper, Scissors and Hangman games with the option 
# to create an account or login.

from hangman import play_hangman
from rock_paper_scissors import play_game

def login_and_create_account():
    """
    Allows users to create an account or login using a username and password.
    """
    # Dictionary to store usernames and passwords
    username_password = {}
    done = False
    while not done:
        print('\033[36m' + '-=' * 20)
        print('1. Create an account')
        print('2. Login') 
        print('-=' * 20 + '\033[0m')

        choice = input('Enter your choice (1 or 2): ')

        if choice == '1': # Create an account
            new_user = False
            while not new_user:

                print('\033[36m' + '-=' * 20)
                print('\t  CREATE AN ACCOUNT')
                print('-=' * 20 + '\033[0m')

                new_username = input('New Username: ').upper().strip()

                # Checking if the username already exists
                try:
                    with open('user.txt', 'r', encoding='utf-8') as file:
                        all_data = file.readlines()
                        for index, data in enumerate(all_data):
                            split_data = data.split(';')
                            if new_username == split_data[0].strip():
                                print('\n\033[31mUser already has an account.\033[0m\n')
                                new_user = True
                                break
                except FileNotFoundError:
                           
                    if not new_user:
                        new_password = input('New Password: ').upper().strip()
                        confirm_password = input('Confirm Password: ').upper().strip()

                        if new_password == confirm_password:
                            print('\nNew user added.\n')
                            username_password[new_username] = new_password

                            # Adding the new username and password to the user.txt file
                            with open('user.txt', 'a', encoding='utf-8') as file:
                                for username, password in username_password.items():
                                    file.write(f'{username}; {password}\n')
                            new_user = True
                            done = True
                        else:
                            print('\n\033[31mPassword does not match.\033[0m\n')
                            continue
        
        elif choice == '2': # Login
            logged_in = False
            while not logged_in:

                print('\n\033[36m' + '-=' * 20)
                print(' \t\t LOGIN')
                print('-=' * 20 + '\033[0m')

                curr_user = input('Username: ').upper().strip()
                curr_pass = input('Password: ').upper().strip()

                # Check if the entered username and password match those stored in the file
                with open('user.txt', 'r', encoding='utf-8') as file:
                    data_user = file.readlines()
                    for index, data in enumerate(data_user):
                        split_string = data.split(';')
                        if curr_user == split_string[0].strip() and curr_pass == split_string[1].strip(): 
                            print('\nLogin Successful!\n')
                            logged_in = True   #  # Exiting the inner loop
                            done = True # Exiting the outer loop
                            break  # Exiting the for loop    
                    else:
                        print('\n\033[31mIncorrect username or password.\033[0m')
        else:
            print('\n\033[31mPlease enter a valid option.\033[0m')
            continue

def main():
    """
    Displays a game menu and allows the user to choose between playing Rock, Paper,
    Scissors, playing Hangman or logging out.
    """
    # Calling the function to handle user authentication
    login_and_create_account()
    
    while True:
        # Printing the game menu options
        print('\033[36m' + '-=' * 20)
        print('\tWelcome to the Game Menu')
        print('1. Play Rock, Paper, Scissors')
        print('2. Play Hangman')
        print('0. Log out')
        print('-=' * 20 + '\033[0m')

        choice = input('Enter your choice: ')

        if choice == '1':
            play_game()
        elif choice == '2':
            play_hangman()
        elif choice == '0':
            print('\nLogging out. Goodbye!')
            break
        else:
            print('\n\033[31mPlease enter a valid option.\033[0m')
                             
if __name__ == "__main__":
    main()         



                
                

             
                


             
               
               
              
                
                
               

            
                                
    

                
                
               



              
    
        


    
