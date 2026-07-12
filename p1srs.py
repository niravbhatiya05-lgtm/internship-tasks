#STUDENT REPEORT SYSTEM
subjects = ("Math", "Science", "English")

students = [
    {"name": "Rahul", "marks": [85, 78, 90]},
    {"name": "Priya", "marks": [65, 70, 60]},
    {"name": "Amit", "marks": [45, 55, 50]}
]

passed_students = set()

def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def calculate_average(marks):
    total = calculate_total(marks)
    average = total / 3
    return average

def check_result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"

def find_topper(students):
    topper = ""
    highest = 0
    for student in students:
        avg = calculate_average(student["marks"])
        if avg > highest:
            highest = avg
            topper = student["name"]
    return topper

print("Student Report")
print()

for student in students:
    total = calculate_total(student["marks"])
    average = calculate_average(student["marks"])
    result = check_result(average)

    if result == "Pass":
        passed_students.add(student["name"])

    print("Name :", student["name"])
    print("Subjects :", subjects)
    print("Marks :", student["marks"])
    print("Total :", total)
    print("Average :", average)
    print("Result :", result)
    print()

print("Passed Students :", passed_students)
print("Topper :", find_topper(students))