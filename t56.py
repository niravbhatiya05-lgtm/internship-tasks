def validate_age():
    try:
        age = int(input("Enter age: "))

        if age >= 18:
            return "Valid age"
        else:
            return "Age must be 18 or above"

    except:
        return "Invalid input"

print(validate_age())