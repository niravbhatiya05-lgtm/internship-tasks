def even_squares(numbers):
    result = []

    for i in numbers:
        if i % 2 == 0:
            result.append(i * i)

    return result

numbers = list(map(int, input("Enter numbers: ").split()))

print(even_squares(numbers))