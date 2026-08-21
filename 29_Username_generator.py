import random

print("=" * 40)
print("       🔐 USERNAME GENERATOR")
print("=" * 40)

adjectives = [
    "Silent",
    "Cyber",
    "Swift",
    "Brave",
    "Lucky",
    "Shadow",
    "Clever",
    "Rapid",
    "Mystic",
    "Digital"
]

animals = [
    "Wolf",
    "Falcon",
    "Tiger",
    "Eagle",
    "Dragon",
    "Lion",
    "Fox",
    "Hawk",
    "Panther",
    "Phoenix"
]

name = input("\nEnter your name: ").strip()

if not name:
    print("❌ Please enter a valid name.")
else:
    print("\n✨ Generated Usernames")
    print("-" * 30)

    usernames = set()

    while len(usernames) < 5:
        adjective = random.choice(adjectives)
        animal = random.choice(animals)
        number = random.randint(10, 99)

        username = f"{adjective}_{name}_{animal}{number}"

        usernames.add(username)

    for number, username in enumerate(usernames, start=1):
        print(f"{number}. {username}")

    print("\n✅ Username generation complete!")