print("🔎 Duplicate Word Finder")
print("------------------------")

text = input("Enter your text: ")

# Convert text to lowercase
text = text.lower()

# Remove common punctuation
punctuation = ".,!?;:()[]{}\"'"

for character in punctuation:
    text = text.replace(character, "")

# Split text into words
words = text.split()

# Count each word
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display results
print("\n📊 Word Frequency")
print("-----------------")

for word, count in word_count.items():
    print(f"{word} → {count} time(s)")

# Find duplicate words
print("\n🔁 Duplicate Words")
print("------------------")

duplicates_found = False

for word, count in word_count.items():
    if count > 1:
        print(f"{word} → {count} times")
        duplicates_found = True

if not duplicates_found:
    print("✅ No duplicate words found!")

print("\n✅ Analysis complete!")