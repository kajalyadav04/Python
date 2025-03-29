# Initialize counters 
positive_count = 0
negative_count = 0

# Read 5 numbers from the user
for i in range(5):
    num = int(input(f"Input the {i + 1} number: "))
    
    # Check if the number is positive, negative, or zero
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

# Display the counts
print(f"Number of positive numbers: {positive_count}")
print(f"Number of negative numbers: {negative_count}")
