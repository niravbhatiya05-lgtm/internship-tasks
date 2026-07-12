numbers = [25, 60, 45, 80, 10, 55, 90, 35]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("List:", numbers)
print("Maximum number:", maximum)