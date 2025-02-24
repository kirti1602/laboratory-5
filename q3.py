# Print first 4 even numbers using continue statement
count = 0
even_count = 0

while count < 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)
    even_count += 1
    if even_count == 4:
        break
