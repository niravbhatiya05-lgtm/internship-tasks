def print_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

def main():
    size = int(input("Enter set size: "))
    numbers = set()

    for i in range(size):
        numbers.add(int(input("Enter element: ")))

    print_even(numbers)

main()