print("🔄 Unit Converter")
print("-----------------")

print("1. Kilometers → Miles")
print("2. Miles → Kilometers")
print("3. Celsius → Fahrenheit")
print("4. Fahrenheit → Celsius")
print("5. Kilograms → Pounds")
print("6. Pounds → Kilograms")

choice = input("\nChoose an option (1-6): ")

value = float(input("Enter value: "))

if choice == "1":
    result = value * 0.621371
    print(f"{value} km = {result:.2f} miles")

elif choice == "2":
    result = value * 1.60934
    print(f"{value} miles = {result:.2f} km")

elif choice == "3":
    result = (value * 9 / 5) + 32
    print(f"{value}°C = {result:.2f}°F")

elif choice == "4":
    result = (value - 32) * 5 / 9
    print(f"{value}°F = {result:.2f}°C")

elif choice == "5":
    result = value * 2.20462
    print(f"{value} kg = {result:.2f} pounds")

elif choice == "6":
    result = value * 0.453592
    print(f"{value} pounds = {result:.2f} kg")

else:
    print("❌ Invalid option.")