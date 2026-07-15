def odd_numbers(data):
    for num in data:
        if num % 2 != 0:
            print(num)

numbers = ()

n = int(input("Enter the number of elements: "))

temp = []

for i in range(n):
    num = int(input("Enter number: "))
    temp.append(num)

numbers = tuple(temp)

odd_numbers(numbers)