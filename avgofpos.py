# Initialize variables for positive numbers and their sum
positive_count = 0
positive_sum = 0

# Read 5 numbers from the user
for i in range(5):
    num = float(input(f"Input the {i + 1} number: "))
    
    # Check if the number is positive
    if num > 0:
        positive_count += 1
        positive_sum += num

# Calculate the average of positive numbers
if positive_count > 0:
    average_positive = positive_sum / positive_count
    print(f"Number of positive numbers: {positive_count}")
    print(f"Average value of the said positive numbers: {average_positive:.2f}")
else:
    print("No positive numbers entered.")
