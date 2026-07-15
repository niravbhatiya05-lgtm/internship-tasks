def print_passed(students):
    for name, marks in students.items():
        if marks >= 35:
            print(name, marks)

def main():
    size = int(input("Enter number of students: "))
    students = {}

    for i in range(size):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    print_passed(students)

main()