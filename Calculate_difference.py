# Function to calculate the difference
def calculate_difference(num):
    if num > 17:
        return 2 * abs(num - 17)
    else:
        return 17 - num

# Accept a number from the user
number = int(input("Enter a number: "))

# Calculate and print the result
result = calculate_difference(number)
print("The result is:", result)
