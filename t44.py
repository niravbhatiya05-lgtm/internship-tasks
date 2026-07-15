keys = input("Enter keys: ").split()
values = input("Enter values: ").split()

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)