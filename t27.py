text = input("Enter a String: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in text:
    if ch >= "A" and ch <= "Z":
        uppercase = uppercase + 1
    elif ch >= "a" and ch <= "z":
        lowercase = lowercase + 1
    elif ch >= "0" and ch <= "9":
        digits = digits + 1
    else:
        special = special + 1

print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special)