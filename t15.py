def print_positive(numbers):
    for num in numbers:
        if num > 0:
            print(num)

def main():
    size = int(input("Enter list size: "))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter element: ")))

    print_positive(numbers)

main()