def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    size = int(input("Enter list size: "))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter element: ")))

    print("Sum:", find_sum(numbers))

main()