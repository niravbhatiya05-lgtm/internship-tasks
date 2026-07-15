def sum_list(numbers):
    print("Sum:", sum(numbers))

def main():
    size = int(input("Enter list size: "))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter element: ")))

    sum_list(numbers)

main()