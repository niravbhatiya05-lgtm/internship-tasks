def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

def main():
    size = int(input("Enter list size: "))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter element: ")))

    print("Positive numbers:", count_positive(numbers))

main()