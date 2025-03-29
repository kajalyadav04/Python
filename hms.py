def convert_seconds_to_hms(seconds):
    # Calculate hours, minutes, andseconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return hours, minutes, remaining_seconds
seconds_input = int(input("Enter the number of seconds: "))
hours, minutes, remaining_seconds = convert_seconds_to_hms(seconds_input)
print(f"{seconds_input} seconds is equal to {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
