num = int(input("Enter a number: "))
last_digit = num % 10
while num >= 10:
    num = num // 10

first_digit = num
print(f"The first digit of the number is: {first_digit}")
print(f"The last digit of the number is: {last_digit}")
