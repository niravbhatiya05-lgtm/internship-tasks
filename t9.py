def check_password(password):
    if len(password) >= 8:
        print("Valid Password")
    else:
        print("Invalid Password")

def main():
    password = input("Enter password: ")
    check_password(password)

main()