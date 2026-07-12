text = input("Enter a string: ")

count = 0

for ch in text:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        count = count + 1

print("Number of vowels:", count)