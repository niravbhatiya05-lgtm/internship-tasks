def count_vowels(characters):
    count = 0
    for ch in characters:
        if ch.lower() in "aeiou":
            count += 1
    print("Vowels:", count)

def main():
    size = int(input("Enter list size: "))
    characters = []

    for i in range(size):
        characters.append(input("Enter character: "))

    count_vowels(characters)

main()