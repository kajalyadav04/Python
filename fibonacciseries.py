terms = int(input("Enter the number of terms in the Fibonacci series: "))
first_term, second_term = 0, 1
print("Fibonacci Series:")
for _ in range(terms):
    print(first_term, end=", ")
    next_term = first_term + second_term
    first_term, second_term = second_term, next_term
