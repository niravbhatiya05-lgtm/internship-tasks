text = input("Enter a string: ")

count = 0

for ch in text:
    if ch >= "A" and ch <= "Z":
        count = count + 1

print("Number of uppercase letters:", count)