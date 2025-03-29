current_char = ord('A')
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(current_char), end=" ")
        current_char += 1
    print()
