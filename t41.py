marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

average = sum(marks) / 5

print("Average marks:", average)