# Use input to get the time (in minutes) for all three events: swimming, cycling, and running.
# Calculate and display the total time taken to complete the triathlon.
# The award a participant receives is based on the total time taken to complete the triathlon.

swimming_time = int(input("Enter the time in minutes taken to complete the swimming event: "))
cycling_time = int(input("Enter the time in minutes taken to complete the cycling event: "))
running_time = int(input("Enter the time in minutes taken to complete the running event: "))

# Calculate total time taken to complete the triathlon.
total_time = (swimming_time + cycling_time + running_time)
print("")
print(f"The total time taken to complete all three events was {total_time} minutes.")

# Check the qualifying criteria.
print("")
if total_time <= 100:
    print("You will receive Provincial Colours.") 
elif total_time > 100 and total_time <= 105:
    print("You will receive Provincial Half Colours.")
elif total_time > 105 and total_time <= 110:
    print("You will receive Provincial Scroll.")    
elif total_time > 110:
    print("Sorry, you will not receive the award.")    




