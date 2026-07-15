numbers = list(map(int, input("Enter numbers: ").split()))

all_prime = True

for num in numbers:
    if num < 2:
        all_prime = False
        break

    for i in range(2, num):
        if num % i == 0:
            all_prime = False
            break

if all_prime:
    print("All numbers are prime")
else:
    print("Not all numbers are prime")