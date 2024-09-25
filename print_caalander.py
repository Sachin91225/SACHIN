import calendar

# Get the month and year from the user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Print the calendar
print(calendar.month(year, month))
