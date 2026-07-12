ch = input("Enter a Character: ")

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
    print("Vowel")
elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
    print("Consonant")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("Special Character")