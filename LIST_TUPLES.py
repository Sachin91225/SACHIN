# Get the input from the user
numbers = input("Enter comma-separated numbers: ")

# Generate a list by splitting the input string
numbers_list = numbers.split(",")

# Generate a tuple from the list
numbers_tuple = tuple(numbers_list)

# Print the results
print("List:", numbers_list)
print("Tuple:", numbers_tuple)
