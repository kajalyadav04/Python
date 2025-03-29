a = int(input("Enter A: "))
b = int(input("Enter B: "))
print("Before Swapping:")
print(f"A = {a} B = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print("After Swapping:")
print(f"A = {a} B = {b}")
