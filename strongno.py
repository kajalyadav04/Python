num = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
original_num = num
sum_of_factorials = 0

while num > 0:
    digit = num % 10
    sum_of_factorials += factorial(digit)
    num = num // 10

if sum_of_factorials == original_num:
    print(f"{original_num} is a Strong Number.")
else:
    print(f"{original_num} is not a Strong Number.")
