month_number = int(input("Input a number between 1 to 12 to get the month name:"))
if 1 <= month_number <= 12:
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    print(f"The month is: {month_names[month_number - 1]}")
else:
    print("Invalid input. Please enter a number between 1 and 12.")
