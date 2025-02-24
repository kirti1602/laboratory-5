# Count the frequency of characters in a string
str = input("Enter a string: ")

# Create a dictionary to store frequency
char_frequency = {}

for char in str:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print the character frequencies
print("Character Frequency:", char_frequency)
