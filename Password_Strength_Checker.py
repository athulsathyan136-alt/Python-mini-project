import string

print("🔐 Password Strength Checker")

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase
if any(char.isupper() for char in password):
    score += 1

# Check lowercase
if any(char.islower() for char in password):
    score += 1

# Check number
if any(char.isdigit() for char in password):
    score += 1

# Check special character
if any(char in string.punctuation for char in password):
    score += 1

# Display result
if score <= 2:
    print("🔴 Password Strength: Weak")
elif score <= 4:
    print("🟡 Password Strength: Medium")
else:
    print("🟢 Password Strength: Strong")

print(f"Score: {score}/5")
# Updated by Athul Sathyan