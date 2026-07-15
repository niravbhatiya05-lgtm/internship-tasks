numbers = list(map(int, input("Enter numbers: ").split()))

for i in numbers:
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")