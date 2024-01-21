# The program collects and stores user information, including name, age and contact details. 
# Admins can view stored user data through a menu system.

import re
import json

def save_user_data(user_data): # Function to save user data to a file in JSON format.
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

# For user input
done = False
user_data = {}

while not done:
    # Role selection, if user or admin
    role = input("Are you a user or an administrator? (Type 'user' or 'admin'): ").lower()
    if role == 'user':

        # User name
        while True:
            def validate_user_name(user_name):
                # Check if the name contains only letters and spaces
                return all(c.isalpha() or c.isspace() for c in user_name)
            # Check if name length is within acceptable limits
            minimum_length = 2
            maximum_length = 50

            user_name = input('Enter your name: ')
            if validate_user_name(user_name) and (minimum_length <= len(user_name) <= maximum_length):
                user_data['name'] = user_name # User data stored in the user_data dictionary.
                break
            else:
                print('The name is invalid!')

        # User age
        while True:
            try:
                user_age = int(input('Enter your age: '))
                user_data['age'] = user_age
                break
            except ValueError:
                print('The age is invalid!')

        # User email address
        while True:
            user_email = input('Enter your email address:(e.g.yourname@mail.com) ')
            # The regular expression validates a basic pattern for an email address.
            email_pattern = r'^\S+@\S+\.\S+$'

            expected_match = re.match(email_pattern, user_email)

            if expected_match:
                user_data['email'] = user_email
                break
            elif user_email == '':
                print('Please enter an email address.')
            else:
                print('The email is invalid!')

        # User cell phone number
        while True:
            user_phone_number = input('Enter your cell phone number: ')
            if len(user_phone_number) == 10 and user_phone_number.isdigit():
                user_data['phone number'] = user_phone_number
                break
            else:
                print('The cell phone number is invalid!')

        # User house number
        while True:
            # Check if the house number length is within acceptable limits
            minimum_length = 1
            maximum_length = 10

            user_house_number = input('Enter your house number: ')
            # Checks if at least one character in the user_house_number is a digit
            if (minimum_length <= len(user_house_number) <= maximum_length) and any(c.isdigit() for c in user_house_number):
                user_data['house number'] = user_house_number
                break
            else:
                print('The house number is invalid!')

        # User street
        while True:
            def validate_user_street(user_street):
                # Check if the street contains only letters and spaces
                return all(c.isalpha() or c.isspace() for c in user_street)
            # Check if the street length is within acceptable limits
            minimum_length = 2
            maximum_length = 20

            user_street = input('Enter your street: ')
            if validate_user_street(user_street) and (minimum_length <= len(user_street) <= maximum_length):
                user_data['street'] = user_street
                break
            else:
                print('The street is invalid!')

        # User city
        while True:
            def validate_user_city(user_city):
                # Check if the city contains only letters and spaces
                return all(c.isalpha() or c.isspace() for c in user_city)
            # Check if city length is within acceptable limits
            minimum_length = 2
            maximum_length = 10

            user_city = input('Enter your city: ')
            if validate_user_city(user_city) and (minimum_length <= len(user_city) <= maximum_length):
                user_data['city'] = user_city
                break
            else:
                print('The city is invalid!')
        save_user_data(user_data) # Save user data to a file
        done = True  # Exiting the outer loop for the user

    elif role == 'admin':
        # For administrator 
        
        def load_user_data(): # Loads user data from a file (if the file exists).
            try:
                with open('user_data.json', 'r') as file:
                    user_data = json.load(file)
                return user_data 
            except FileNotFoundError: # Handle the case where the file doesn't exist
                return {}
        
        def admin_menu():
            while True:
                print('\nAdmin Menu:')
                print('1. View User Data')
                print('2. Exit Admin Menu')

                admin_choice = input('Enter your choice: ')

                if admin_choice == '1':
                    view_user_data() # Prints user data stored in the user_data dictionary.
                elif admin_choice == '2':
                    print('Exiting Admin Menu.')
                    break
                else:
                    print('Invalid choice. Please enter a valid option.')
        done = True  # Exiting the outer loop for the admin

        user_data = load_user_data()
        
        def view_user_data():
        # Prints the user data stored in the user_data dictionary.
            print('\nUser Data:')
            for key, value in user_data.items():
                print(f'{key.capitalize()}: {value}')
        
        admin_menu()  # Call the admin_menu function  

    else:
        print('Invalid role. Please enter "user" or "admin".')


