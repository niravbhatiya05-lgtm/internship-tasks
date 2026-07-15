def check_number(num):
    if num.is_integer():
        print("Whole number")
    else:
        print("Decimal number")

def main():
    number = float(input("Enter a float: "))
    check_number(number)

main()