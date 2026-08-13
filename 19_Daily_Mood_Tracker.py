from datetime import date

print("😊 Daily Mood Tracker")

mood = input("How are you feeling today? ")

today = date.today()

with open("mood_history.txt", "a") as file:
    file.write(f"{today} - {mood}\n")

print(f"✅ Mood saved for {today}!")