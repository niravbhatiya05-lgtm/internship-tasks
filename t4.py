def check_eligibility(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

def main():
    age = int(input("Enter age: "))
    check_eligibility(age)

main()