numbers = []
even = []
odd = []

for i in range(5):
    num = int(input("Enter Number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Numbers:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)