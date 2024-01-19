# Shopping cart application for pet-related products.

from tabulate import tabulate

done = False
cart_list = []

while (not done):
    print('')
    print('Welcome to Paws n Cart!\n')
    print('-' * 80)
    print('This is your shopping cart:')
    print(f'Whiskers Cat Food \t\t R {'':2} 20.00 ')
    print(f'Dog Kong \t\t\t R {'':2} 50.00')
    print(f'Lucerne Hay \t\t\t R {'':2} 150.00')
    print('-' * 80)
    print('Would you like to:\n'
      '1. Add an item to your cart\n'
      '2. Remove an item from your cart\n'
      '3. View the cart\n'
      '4. Checkout\n'
      '5. Exit')
    choice = input('Enter the number of the option you would like to choose:\n')
    
    if choice == '1': # Find out item, quantity and prices and add it to cart list
        items_info = {
                'WHISKERS CAT FOOD': 20.00,
                'DOG KONG': 50.00,
                'LUCERNE HAY': 150.00}
        
        item = input('What item would you like to add to your cart? ').upper().strip()
        
        try: # To handle potential error when user enter invalid input
            quantity = int(input('Enter the quantity: '))
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue

        if item in items_info:
            price_per_unit = int(items_info[item])
            total_product_price = int(price_per_unit * quantity)
            
            # Check if the item is in the cart
            existing_item = next((item_info for item_info in cart_list if item_info.get('Item') == item), None)
        
            if existing_item:
                existing_item['Quantity'] += quantity
                existing_item['Total product price'] += total_product_price
            else: # Add a new item to cart. A dictionary representing the selected item is appended to the cart_list.  
                cart_list.append({'Item': item, 'Price per unit': price_per_unit, 'Quantity': quantity, 'Total product price': total_product_price})
 
            print(f'{item} has been added to your cart successfully.')
        else:
            print(f'{item} is not found in the menu.')

    elif choice == '2': # Remove item from cart list
        remove_item = input('Which item would you like to remove? ').upper().strip()
        current_quantity = sum(item_info.get('Quantity', 0) for item_info in cart_list if item_info.get('Item') == remove_item)
       
        # For loop to remove occurrences of the key
        removed = False
        
        for item_info in cart_list[:]:
            if item_info.get('Item') == remove_item:
                quantity_remove = int(input(f'How many units of {remove_item} would you like to remove? (Current quantity: {current_quantity}): '))
                
                # Checks if the quantity to be removed is valid
                if 1 <= quantity_remove <= current_quantity:
                    item_info['Quantity'] -= quantity_remove
                    item_info['Total product price'] -= quantity_remove * item_info['Price per unit']   
                    removed = True
                    print(f'{quantity_remove} unit{"s" if quantity_remove > 1 else ""} of {remove_item} {"have" if quantity_remove > 1 else "has"} been removed from your cart successfully.')
                
                # Remove the item completely
                    if item_info['Quantity'] == 0:
                        cart_list.remove(item_info)
                        print(f'{remove_item} has been removed from your cart successfully.')
                else:
                    print(f'Invalid quantity. Please enter a quantity between 1 and {current_quantity}.')    
        if not removed:
            print('That item is not in your cart.')

    elif choice == '3': # Display cart summary
        if not cart_list:  # Check if the shopping cart is empty.
            print('Your shopping cart is empty.')
        else: # Display cart
            print('This is your shopping cart:')
            # Add individual items to cart
            table = tabulate(cart_list, headers = 'keys', tablefmt = 'fancy_grid', colalign = ('center', 'center', 'center', 'center'))
            print(table)  

    elif choice == '4': # Display total cart summary
        if not cart_list:  # Check if the shopping cart is empty.
            print('Your shopping cart is empty.')
        else: # Display cart
            # Removes the existing total line
            cart_list = [item_info for item_info in cart_list if item_info.get('Item') != 'Total']
  
            # New total
            total_cart = sum(item_info.get('Total product price', 0) for item_info in cart_list)
            
            # Add the total line to the cart
            total_row = {'Item': 'Total', 'Price per unit': '', 'Quantity': '', 'Total product price': total_cart}
            cart_list.append(total_row)
            
            print('That is the total summary of your shopping cart:\n')
            table_with_total = tabulate(cart_list, headers = 'keys', tablefmt = 'fancy_grid', colalign = ('center', 'center', 'center', 'center'))
            print(table_with_total)
            print('Thank you for shopping with Paws n Cart!')
    
    elif choice == '5':
        print('Exiting Paws n Cart. Goodbye!')
        done = True
    else:
        print('That is not a valid option. Please choose a number from 1 to 5.')

            
        
        
     

    
    
    



    




      

    
   


