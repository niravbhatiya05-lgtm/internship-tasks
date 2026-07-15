def calculate_grade(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

def main():
    marks = float(input("Enter marks: "))
    calculate_grade(marks)

main()