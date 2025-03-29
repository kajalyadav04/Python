# Initialize the sum of odd values
sum_of_odd = 0

# Read 5 numbers from the user
for i in range(5):
    num = int(input(f"Input the {i + 1} number: "))
    
    # Check if the number is odd
    if num % 2 != 0:
        sum_of_odd += num

# Display the sum of odd values
print(f"Sum of all odd values: {sum_of_odd}")
