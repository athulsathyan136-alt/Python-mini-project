import random

print("🎲 Dice Roller")
print("-------------")

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)

    print("You rolled:", dice)

    again = input("Roll again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing! 👋")
        break