import random

print("=" * 40)
print("      😊 MOOD ACTIVITY SUGGESTER")
print("=" * 40)

activities = {
    "happy": [
        "Call a friend and share your happiness.",
        "Go for a walk and enjoy the weather.",
        "Listen to your favorite music.",
        "Work on a fun personal project."
    ],

    "sad": [
        "Talk to someone you trust.",
        "Watch a funny movie or video.",
        "Listen to some relaxing music.",
        "Go outside and get some fresh air."
    ],

    "tired": [
        "Take a short 20-minute rest.",
        "Drink some water and stretch.",
        "Take a relaxing shower.",
        "Go to bed early tonight."
    ],

    "stressed": [
        "Take 5 minutes for deep breathing.",
        "Go for a short walk.",
        "Listen to calm music.",
        "Take a break from your screen."
    ],

    "bored": [
        "Learn something new for 15 minutes.",
        "Try a small Python project.",
        "Read a few pages of a book.",
        "Clean and organize your workspace."
    ]
}

print("\nHow are you feeling?")
print("1. 😊 Happy")
print("2. 😢 Sad")
print("3. 😴 Tired")
print("4. 😰 Stressed")
print("5. 😐 Bored")

choice = input("\nChoose an option (1-5): ")

mood_options = {
    "1": "happy",
    "2": "sad",
    "3": "tired",
    "4": "stressed",
    "5": "bored"
}

if choice in mood_options:
    mood = mood_options[choice]

    suggestion = random.choice(activities[mood])

    print("\n" + "-" * 40)
    print("Your mood:", mood.capitalize())
    print("💡 Suggested Activity:")
    print(suggestion)
    print("-" * 40)

else:
    print("\n❌ Invalid choice!")
    print("Please choose a number from 1 to 5.")

print("\nThank you for using Mood Activity Suggester! 😊")
