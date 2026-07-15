def find_largest(a, b, c):
    if a >= b and a >= c:
        print("Largest number:", a)
    elif b >= a and b >= c:
        print("Largest number:", b)
    else:
        print("Largest number:", c)

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    find_largest(num1, num2, num3)

main()