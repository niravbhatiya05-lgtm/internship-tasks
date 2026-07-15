def process_numbers():
    try:
        numbers = list(map(int, input("Enter numbers: ").split()))

        even_numbers = []

        for i in numbers:
            if i % 2 == 0:
                even_numbers.append(i)
            else:
                print(i, "is odd")

        return even_numbers

    except:
        return "Invalid input"

print(process_numbers())