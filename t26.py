set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Common Elements:")

for i in set1:
    if i in set2:
        print(i)

print("Unique Elements of Set 1:")

for i in set1:
    if i not in set2:
        print(i)

print("Unique Elements of Set 2:")

for i in set2:
    if i not in set1:
        print(i)