try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)

finally:
    print("Program Ended.")