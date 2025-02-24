# Change all occurrences of the first character to '$' except the first one
str = input("Enter a string: ")

if len(str) > 1:
    first_char = str[0]
    str = first_char + str[1:].replace(first_char, '$')
    print("Modified string:", str)
else:
    print("String is too short.")
