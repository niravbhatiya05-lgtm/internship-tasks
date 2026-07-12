text = input("Enter a string: ")

count = 0

for ch in text:
    if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        if ch != "a" and ch != "e" and ch != "i" and ch != "o" and ch != "u" and ch != "A" and ch != "E" and ch != "I" and ch != "O" and ch != "U":
            count = count + 1

print("Number of consonants:", count)