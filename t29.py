def remove_duplicates(numbers):
    unique_numbers = set()

    for num in numbers:
        unique_numbers.add(num)

    print("Unique Values:")

    for num in unique_numbers:
        print(num)

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

remove_duplicates(numbers)