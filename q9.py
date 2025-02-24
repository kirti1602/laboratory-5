# Swap the first two characters of two strings and combine them
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) >= 2 and len(str2) >= 2:
    str1_swapped = str2[:2] + str1[2:]
    str2_swapped = str1[:2] + str2[2:]
    result = str1_swapped + " " + str2_swapped
    print("Resulting string:", result)
else:
    print("Both strings must have at least 2 characters.")
