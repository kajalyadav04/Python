sum_of_odd = 0
for i in range(5):
    num = int(input(f"Input the {i + 1} number: "))
    if num % 2 != 0:
        sum_of_odd += num
print(f"Sum of all odd values: {sum_of_odd}")
