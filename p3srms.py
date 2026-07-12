name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input("Enter Mark: "))
    marks.append(mark)

marks_tuple = tuple(marks)

total = 0

for mark in marks_tuple:
    total = total + mark

average = total / 5

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

student = {
    "name": name,
    "marks": marks_tuple,
    "total": total,
    "average": average,
    "grade": grade
}

unique_marks = set(marks_tuple)

passed = False

if average >= 50:
    passed = True

print("\nStudent Report")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", student["total"])
print("Average:", student["average"])
print("Grade:", student["grade"])
print("Unique Marks:", unique_marks)
print("Passed:", passed)