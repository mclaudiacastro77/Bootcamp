# Create a program that reads 5 numeric values and stores them in a list.
# At the end, show which was the maximum and minimum value entered and the
# their respective positions in the list.

values = []
for cont in range(0,5):
    values.append(int(input(f"Enter a value for the position {cont}: ")))

print("=-" * 30)
print(f"You entered the values {values}.")
print(f"The maximum value is: {max(values)} in the positions ", end="")
for i, v in enumerate(values):
    if v == max(values):
        print(f"{i}...", end="")

print(f"\nThe minimum value is: {min(values)} in the positions ", end="")
for i, v in enumerate(values):
    if v == min(values):
        print(f"{i}...", end="")