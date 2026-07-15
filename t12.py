def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial:", fact)

def main():
    number = int(input("Enter a number: "))
    factorial(number)

main()