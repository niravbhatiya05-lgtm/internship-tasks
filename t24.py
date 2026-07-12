students = []

for i in range(3):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

print("Passed Students:")

for student in students:
    if student["marks"] >= 35:
        print(student["name"])