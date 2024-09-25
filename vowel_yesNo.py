# Function to check if a letter is a vowel
def is_vowel(letter):
    return letter.lower() in 'aeiou'

# Accept a letter from the user
letter = input("Enter a letter: ")

# Check and print the result
if len(letter) == 1 and letter.isalpha():
    if is_vowel(letter):
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")
else:
    print("Please enter a single alphabetical character.")
