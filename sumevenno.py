n = int(input("Enter a number (n): "))
even_sum = 0
for num in range(2, n + 1, 2):
    even_sum += num
print(f"The sum of even numbers between 1 and {n} is: {even_sum}.")
