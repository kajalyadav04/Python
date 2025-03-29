num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 < num2 < num3:
    print("Increasing")
elif num1 > num2 > num3:
    print("Decreasing")
else:
    print("Neither increasing nor decreasing order")
