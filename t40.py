def get_number():
    try:
        num = int(input("Enter number: "))
        return num
    except:
        return "Invalid input"

print(get_number())