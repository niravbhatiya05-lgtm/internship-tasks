student = {
    "name": input("Enter Name: "),
    "marks": []
}

total = 0

for i in range(5):
    mark = int(input("Enter Mark: "))
    student["marks"].append(mark)

for mark in student["marks"]:
    total = total + mark

average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", total)
print("Average:", average)
print("Grade:", grade)