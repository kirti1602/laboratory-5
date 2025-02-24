# Print first 5 even numbers using break statement
count = 0
even_count = 0

while count < 10:
    if count % 2 == 0:
        print(count)
        even_count += 1
    count += 1
    if even_count == 5:
        break
