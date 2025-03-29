num = int(input("Enter a number: "))
last_digit = num % 10
num_digits = 0
temp_num = num
while temp_num > 0:
    temp_num = temp_num // 10
    num_digits += 1
first_digit = num // 10**(num_digits - 1)
num_without_first_last = (num % 10**(num_digits - 1)) // 10
swapped_num = last_digit * 10**(num_digits - 1) + num_without_first_last * 10 + first_digit
print(f"Original number: {num}")
print(f"Number after swapping first and last digits: {swapped_num}")
