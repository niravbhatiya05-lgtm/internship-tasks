def check_number(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def main():
    number = int(input("Enter a number: "))
    check_number(number)

main()