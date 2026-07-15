numbers = []

n = int(input("How many values: "))

for i in range(n):
    value = int(input("Enter value: "))
    numbers.append(value)

print("Maximum value:", max(numbers))