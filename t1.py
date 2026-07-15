def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def main():
    number = int(input("Enter an integer: "))
    check_number(number)

main()