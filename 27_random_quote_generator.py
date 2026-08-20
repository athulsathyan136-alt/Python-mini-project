import random

print("💡 Random Quote Generator")
print("-------------------------")

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Don't stop when you're tired. Stop when you're done.",
    "The best way to learn programming is to practice.",
    "Every expert was once a beginner.",
    "Code today, improve tomorrow.",
    "Small progress is still progress.",
    "Believe you can and you're halfway there.",
    "Learning never stops.",
    "Build projects, not just tutorials.",
    "Consistency beats motivation."
]

quote = random.choice(quotes)

print("\n💬 Your Quote:")
print(f'"{quote}"')