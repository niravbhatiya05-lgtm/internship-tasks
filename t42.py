numbers = tuple(map(int, input("Enter tuple values: ").split()))

positive = True

for i in numbers:
    if i <= 0:
        positive = False
        break

if positive:
    print("All values are positive")
else:
    print("Not all values are positive")