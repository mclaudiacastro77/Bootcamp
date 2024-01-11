# Create a program that reads the name and weight of several people,
# saving everything in a list. At the end, show:
# A How many people were registered.
# B A list of the heaviest people.
# C A list of the lightest people.

people = []
data = []
max_weight = min_weight = 0

# Loop to collect data from users
while True:
    data.append(str(input("Enter your name: ")))
    data.append(float(input("Enter your weight: ")))
    if len(people) == 0: # Check if it's the first person entered
        max_weight = min_weight = data[1]
    else: # Update max_weight and min_weight if necessary
        if data[1] > max_weight:
            max_weight = data[1]
        if data[1] < min_weight:
            min_weight = data[1]
    people.append(data[:]) # Add a copy of the data to the people list
    data.clear()
    answer = str(input("Do you want to continue? [S/N] "))
    if answer in "Nn":
        break
print("-=" * 30)
print(people)    
print(f"You registered {len(people)} people.")

# Display the person(s) with the biggest weight
print(f"The biggest weight was {max_weight} KG. Weight of ", end="")
for person in people:
    if person[1] == max_weight:
        print(f"[{person[0]}] ", end="")
print()
# Display the person(s) with the lowest weight
print(f"The lowest weight was {min_weight} KG. Weight of ", end="")
for person in people:
    if person[1] == min_weight:
        print(f"[{person[0]}] ", end="")