# Function to check if the number is within 100 of 1000 or 2000
def is_within_100_of_1000_or_2000(num):
    return (abs(num - 1000) <= 100) or (abs(num - 2000) <= 100)

# Accept a number from the user
number = int(input("Enter a number: "))

# Check and print the result
if is_within_100_of_1000_or_2000(number):
    print(f"{number} is within 100 of 1000 or 2000.")
else:
    print(f"{number} is not within 100 of 1000 or 2000.")
