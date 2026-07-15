def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("Maximum:", maximum)

def main():
    size = int(input("Enter tuple size: "))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter element: ")))

    data = tuple(numbers)
    find_max(data)

main()