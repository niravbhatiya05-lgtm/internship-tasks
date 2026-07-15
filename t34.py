numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Invalid input.")