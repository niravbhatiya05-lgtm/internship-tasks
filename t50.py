def sort_set(values):
    return sorted(list(values))

numbers = set(map(int, input("Enter set values: ").split()))

print(sort_set(numbers))