# The program manages shipping logs, enabling the display and analysis of shipment records. 
# It provides an interactive menu to choose between viewing logs by month or analyzing based on the selected row.

from tabulate import tabulate

class ShippingManager:
    def __init__(self, date, log_entry, tracking_number, location, goods):
        # Initialize with shipment details and an empty list for logs.
        self.date = date
        self.log_entry = log_entry
        self.tracking_number = tracking_number
        self.location = location
        self.goods = goods    
        self.logs = []

    def display_logs(self, filename):
        # Display shipping logs in a table by reading from the specified file and printing each log.
        table = []
        with open(filename, 'r', encoding='utf-8') as file:
                self.logs = file.readlines()
                
                for index, log in enumerate(self.logs, start=1):
                    split_string = log.split('|') # Split the log string using the '|' character as a delimiter.
                    table.append([index,
                          split_string[0].strip(), # Each element in split_string corresponds to a specific field in the log.
                          split_string[1].strip(),
                          split_string[2].strip(),
                          split_string[3].strip(),
                          split_string[4].strip()])

        headers = ['Index','Date', 'LOG', 'Tracking Number', 'Location', 'Goods']
        print(tabulate(table, headers = headers, tablefmt ='fancy_grid', colalign = ('center','center', 'center', 'center', 'center', 'center')))  
   
    def analyze_logs(self, log_index):
        # Display the data from the table based on the row selected by the user.
        if 0 <= log_index < len(self.logs): 
            log = self.logs[log_index]
            # Retrieves the log entry at the specified index (log_index) from the list self.logs.
            split_string = log.split('|')
            # Then, it splits the log entry into individual components using '|' for row analysis.
           
            date = split_string[0].strip()
            log_entry = split_string[1].strip()
            tracking_number = split_string[2].strip()
            location = split_string[3].strip()
            goods = split_string[4].strip()

            # Display details of the selected index.
            print(f'\nDate: {date}\n'
                f'LOG: {log_entry}\n'
                f'Tracking Number: {tracking_number}\n'
                f'Location: {location}\n'
                f'Goods: {goods}\n')

        else:
            print('\nInvalid index. Please provide a valid index.\n')

    def main_menu(self):
        # Display the main menu for the shipping log management tool.
        print('\n\033[34m===== Shipping Log Management Tool =====')
        print('1. Display Shipping Logs')
        print('2. Analyze Shipping Logs')
        print('3. Exit')
        print('========================================\033[0m')

# Creating an instance of the ShippingManager class with empty default values.
shipping_manager = ShippingManager("", "", "", "", "") 
done = False

while not done:
    shipping_manager.main_menu()
    menu_choice = input('Enter your choice (1-3): ')

    if menu_choice == '1': # Display Shipping Logs
        filename = ''
        while True:
            # Display the menu for selecting a month to view logs.
            print('\n\033[92m================= Month =================')
            print('1. January\n'
                  '2. February\n'
                  '3. March\n'
                  '4. Back to Main Menu')
            print('=========================================\033[0m')

            month_menu = input('Choose a option (1-4): ')
            print()

            # Set the filename based on the selected month or exit the inner loop.
            if month_menu == '1':
                filename = 'january.txt'
            elif month_menu == '2':
                filename = 'february.txt'
            elif month_menu == '3':
                filename = 'march.txt'
            elif month_menu == '4':
                break  # Exit the inner loop
            else:
                print('Invalid option. Please choose a valid option.')
                continue
            shipping_manager.display_logs(filename)

    elif menu_choice == '2': # Analyze Shipping Logs
        while True:
            chosen_index = int(input('Enter the index of the log you want to analyze (or enter 0 to go back to the main menu): '))
           
            if chosen_index == 0:
                break  # Exit the inner loop and return to the main menu 
            else:
                shipping_manager.analyze_logs(chosen_index - 1)

    elif menu_choice == '3': # Exit the program
        print('\nExiting the program. Goodbye!')
        done = True
        
    else: # Handle invalid menu choices
        print('\nInvalid choice. Please enter a valid option.')

