def check_case(ch):
    if ch.isupper():
        print("Uppercase")
    elif ch.islower():
        print("Lowercase")
    else:
        print("Not an alphabet")

def main():
    character = input("Enter a character: ")
    check_case(character)

main()