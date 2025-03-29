def convert_days_to_ymd(days):
    years = days // 365
    months = (days % 365) // 30
    remaining_days = (days % 365) % 30
    return years, months, remaining_days
days_input = int(input("Enter the number of days: "))
years, months, remaining_days = convert_days_to_ymd(days_input)
print(f"{days_input} days is equal to {years} years, {months} months, and {remaining_days} days.")
