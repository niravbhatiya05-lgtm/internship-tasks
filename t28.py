def print_keys(data):
    for key in data:
        if data[key] > 50:
            print(key)

student = {}

n = int(input("Enter the number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    student[key] = value

print_keys(student)