numbers = [25, 60, 45, 80, 10, 55, 90, 35]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("List:", numbers)
print("Minimum number:", minimum)