def check_character(ch):
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

def main():
    character = input("Enter a character: ")
    check_character(character)

main()