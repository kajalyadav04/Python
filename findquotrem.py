# Read two integers from the user
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Calculate integral quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

#result
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
