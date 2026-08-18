print("📝 Text Analyzer")
print("----------------")

text = input("Enter your text: ")

# Count characters
character_count = len(text)

# Count words
words = text.split()
word_count = len(words)

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

# Count sentences
sentence_count = 0

for character in text:
    if character in ".!?":
        sentence_count += 1

# Find longest word
if words:
    longest_word = max(words, key=len)
else:
    longest_word = "None"

# Display results
print("\n📊 Text Analysis")
print("----------------")
print("Characters:", character_count)
print("Words:", word_count)
print("Vowels:", vowel_count)
print("Sentences:", sentence_count)
print("Longest word:", longest_word)

print("\n✅ Analysis complete!")