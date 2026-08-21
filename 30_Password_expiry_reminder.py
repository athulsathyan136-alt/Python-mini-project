from datetime import datetime, timedelta

print("==============================")
print("    PASSWORD EXPIRY REMINDER")
print("==============================")

password_date = input("Enter password creation date (YYYY-MM-DD): ")
expiry_days = int(input("Enter password validity in days: "))

try:
    created_date = datetime.strptime(password_date, "%Y-%m-%d")
    expiry_date = created_date + timedelta(days=expiry_days)
    today = datetime.now()

    remaining_days = (expiry_date - today).days

    print("\nPassword Expiry Date:", expiry_date.strftime("%Y-%m-%d"))

    if remaining_days > 0:
        print(f"✅ Password expires in {remaining_days} days.")
    elif remaining_days == 0:
        print("⚠️ Password expires today!")
    else:
        print(f"❌ Password expired {-remaining_days} days ago.")

except ValueError:
    print("❌ Invalid date format.")
    print("Please use YYYY-MM-DD.")