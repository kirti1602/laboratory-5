# Add 'ing' or 'ly' at the end of a string
str = input("Enter a string: ")

if len(str) >= 3:
    if str.endswith("ing"):
        str += "ly"
    else:
        str += "ing"
    print("Modified string:", str)
else:
    print("The string is too short.")
