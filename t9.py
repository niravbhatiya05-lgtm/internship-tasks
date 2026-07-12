numbers = (10, 25, 15, 30, 5, 18, 40, 12)

count = 0

for num in numbers:
    if num < 20:
        count = count + 1
print("Tuple:", numbers)
print("Count of numbers less than 20:", count)