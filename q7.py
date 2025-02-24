# Get the first 2 and last 2 characters from a given string
str = input("Enter a string: ")

if len(str) < 2:
    print("String is too short.")
else:
    result = str[:2] + str[-2:]
    print("Resulting string:", result)
