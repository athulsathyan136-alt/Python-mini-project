print("🔐 Login Attempt Tracker")
print("------------------------")

# Correct login details
correct_username = "admin"
correct_password = "admin123"

max_attempts = 3
attempts = 0

while attempts < max_attempts:

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("\n✅ Login successful!")
        print(f"Welcome, {username}!")
        break

    attempts += 1
    remaining = max_attempts - attempts

    print("\n❌ Incorrect username or password.")

    if remaining > 0:
        print(f"⚠️ Attempts remaining: {remaining}")
    else:
        print("🔒 Account locked!")
        print("Too many failed login attempts.")

print("\nProgram finished.")
