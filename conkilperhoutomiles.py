# Read speed in kilometers per hour from the user
km_per_hour = float(input("Input kilometers per hour: "))

# Conversion factor: 1 kilometer = 0.621371 miles
miles_per_hour = km_per_hour * 0.6213
print(f"{km_per_hour} kilometers per hour is equal to {miles_per_hour} miles per hour.")
