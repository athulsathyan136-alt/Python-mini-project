print("🎓 Student Grade Calculator")
print("---------------------------")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

result = "PASS" if average >= 40 else "FAIL"

print("\n📋 Result")
print("---------------------------")
print(f"Student : {name}")
print(f"Total   : {total}/500")
print(f"Average : {average:.2f}")
print(f"Grade   : {grade}")
print(f"Result  : {result}")