# Get the filename from the user
filename = input("Enter the filename: ")

# Split the filename by the dot and get the extension
file_extension = filename.split(".")[-1]

# Print the file extension
print("Extension of the file:", file_extension)
