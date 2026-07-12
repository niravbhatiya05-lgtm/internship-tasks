students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88
}

topper = ""
highest = 0

for name in students:
    if students[name] > highest:
        highest = students[name]
        topper = name

print("Topper:", topper)
print("Marks:", highest)