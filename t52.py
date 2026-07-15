text = input("Enter string: ")

reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not palindrome")