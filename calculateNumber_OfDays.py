from datetime import date

# Define the two dates
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

# Calculate the difference in days
difference = (date2 - date1).days

# Print the result
print(f"{difference} days")
