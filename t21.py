def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def main():
    number = int(input("Enter a number: "))
    check_even_odd(number)

main()