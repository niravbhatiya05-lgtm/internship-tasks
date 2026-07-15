student = {}

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

try:
    search_key = input("Enter key to search: ")
    print("Value:", student[search_key])

except KeyError:
    print("Key not found.")
    