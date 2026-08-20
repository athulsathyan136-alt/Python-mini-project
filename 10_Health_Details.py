print("===== Health Details =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)

print("\n===== Your Details =====")
print("Name:", name)
print("Age:", age)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))