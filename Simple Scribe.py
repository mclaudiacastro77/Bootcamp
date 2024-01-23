# Simple word-processing tool which allows users to create and edit documents. 
# Once the user has inputted the desired text into the document, the following 
# features will be offered to the user: styles, text formatting and a find-and-replace tool.

import json

def save_to_json(user_text, filename): # Function to save user text to a JSON file
    with open(filename, 'w') as file:
        json.dump({'text': user_text}, file)

def load_user_text(filename): # Load user text from JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('text', '')
    except FileNotFoundError: 
        return None
    
def load_formatted_text(filename): # Load formatted text from JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('text', '')
    except FileNotFoundError:
        return None

# Constants for text formatting 
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'
OFF = '\033[0m'
        
def apply_formatting(loaded_formatted_text, third_menu):
# Apply formatting based on user choice in Edit Document option  
    if third_menu == '1':
        return f'{loaded_formatted_text.upper()}'  # Capitalize
    elif third_menu == '2':
        return f'{BOLD}{loaded_formatted_text}{OFF}'  # Bold
    elif third_menu == '3':
        return f'{UNDERLINE}{loaded_formatted_text}{OFF}'  # Underline
    elif third_menu == '4':
        return f'{ITALIC}{loaded_formatted_text}{OFF}'  # Italicize
    else:
        print('\nInvalid option. Please choose a valid option.')
        print('Text not modified: ',end='')
        return loaded_formatted_text

filename = "document.json"
done = False

# Main program loop
while not done:
    print('')
    print('----- Text Editor Menu -----')
    print('1. Add Text\n'
          '2. Apply Styles\n'  
          '3. Edit Document\n'
          '4. Find and Replace\n'
          '5. Print Document\n'
          '6. Exit')
    menu_choice = input('Enter your choice (1-6): ')

    if menu_choice == '1': # Add Text
    # Prompts the user to input text and saves it to the document if valid.  
        
        while True:  # Inner loop for text input
            user_text = input('Enter the text to add to the document: ').strip()
            if len(user_text) >=1:
                save_to_json(user_text, filename)
                print('Text added successfully.')
                break 
            else:
                print('Please enter a text.')
    
    elif menu_choice == '2': # Apply Styles
    # Offers style options, applies the selected style to the text and save it to the document.
        
        while True:   
            print('')
            print('1. Heading (##)\n'
                  '2. Body (No formatting)\n'
                  '3. Back to Main Menu\n')
            loaded_text = load_user_text(filename)
            if loaded_text is None:
                print('No text available. Please add text first.')
                break

            second_menu = input('Choose a style option (1-3): ')
            
            if second_menu == '1': # Heading
                formatted_text = f'## {loaded_text}'
            elif second_menu == '2': # Body
                formatted_text = f'{loaded_text.lstrip("##").strip()}'
            elif second_menu == '3':
                break  # Exit the inner loop
            else:
                print('\nInvalid option. Please choose a valid option.')
                continue
       
            save_to_json(formatted_text, filename)
            print(formatted_text)
    
    elif menu_choice == '3': # Edit Document
    # Displays formatting options, applies the chosen formatting to the text and
    # save it to the document or returns the original text if an invalid option is selected. 
        
        while True:   
            print('')
            print('1. Capitalize\n'  
                  '2. Bold\n' 
                  '3. Underline\n'
                  '4. Italicize\n'
                  '5. Back to Main Menu\n')
            loaded_formatted_text = load_formatted_text(filename)
            if loaded_formatted_text is None:
                print('No text available. Please add text first.')
                break
            
            third_menu = input('Choose a formatting option (1-5): ')
        
            if third_menu == '5':
                break  # Exit the inner loop
          
            # Call the apply_formatting function to apply formatting to the text
            formatted_text = apply_formatting(loaded_formatted_text, third_menu)
            save_to_json(formatted_text, filename)
            print(formatted_text)
            
    elif menu_choice == '4': # Find and replace
    # Prompts the user to enter text to find and replace within the text.
    # Checks if the entered text exists in the text before performing the replacement.
    # Displays the replaced text and saves it to the document.

        while True:
            loaded_formatted_text = load_formatted_text(filename)
            if loaded_formatted_text is None:
                print('\nNo text available. Please add text first.')
                break
            else:
                print(f'\nThat is your text: {loaded_formatted_text}')  
                original_text = input('Enter the text to find: ')
                
                if original_text not in loaded_formatted_text:
                    print('\nPlease enter the exact text you previously entered.\n'
                         'For example, if you input "HOME," you need to use "HOME" to find.')
                    continue 
                
                replaced_text = input('Enter the replacement text: ')    
                final_text = loaded_formatted_text.replace(original_text, replaced_text)
                
                save_to_json(final_text, filename)
                print('Text replaced successfully.')
                print(f'\nThat is your replaced text: {final_text}')
                break

    elif menu_choice == '5': # Print Document
    # Prints the document content or notifies the user if no text is available.
       
        while True:
            loaded_formatted_text = load_formatted_text(filename)
            if loaded_formatted_text is None:
                print('\nNo text available. Please add text first.')
                break
            else:
                print('\n----- Document Content -----')
                loaded_formatted_text = load_formatted_text(filename)
                print(loaded_formatted_text)
                break

    elif menu_choice == '6': # Exit
        print('\nExiting Simple Scribe. Goodbye!')
        done = True
    
    else:
        print('\nThat is not a valid option. Please choose a number from 1 to 6.')