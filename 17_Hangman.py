import random

def main():
    words = ["python", "java", "kotlin", "javascript", "github", "terminal", "linux"]
    word = random.choice(words).lower()
    guessed = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        # Build current display
        display = "".join([c if c in guessed else "_" for c in word])
        print("\nWord:", display)
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed)))

        if "_" not in display:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    main()