# Create a program where the user can enter numerical values and add them
# in a list. If the number already exists, it will not be added.
# At the end, all unique values entered will be displayed in ascending order.

numbers = []
while True:
    n = int(input("Enter a value: "))
    if n not in numbers:
        numbers.append(n)
        print("Value added successfully.")
    else:
        print("Duplicate value. I will not add it.")
    answer = str(input("Do you want to continue? [S/N] "))
    if answer in "Nn":
        break
print("=-" * 30)   
numbers.sort() # Sort the elements of a list in ascending order.
print(f"You entered the numbers {numbers}.")


