numbers = [10, -5, 20, -15, 0, 30, -8, 12]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

print("List:", numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)