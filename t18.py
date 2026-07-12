marks = (
    int(input("Enter Marks 1: ")),
    int(input("Enter Marks 2: ")),
    int(input("Enter Marks 3: ")),
    int(input("Enter Marks 4: ")),
    int(input("Enter Marks 5: "))
)

total = 0

for mark in marks:
    total = total + mark

average = total / 5

print("Average:", average)

if average >= 50:
    print("Pass")
else:
    print("Fail")