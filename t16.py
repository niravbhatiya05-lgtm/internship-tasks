name = input("Enter Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height: "))
is_student = input("Is Student (True/False): ")

if age >= 18:
    print("Adult")
else:
    print("Minor")