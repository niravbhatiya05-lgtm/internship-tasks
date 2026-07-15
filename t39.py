def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count += 1

    return count

numbers = list(map(int, input("Enter numbers: ").split()))

print("Even numbers count:", count_even(numbers))