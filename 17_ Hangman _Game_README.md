# 🪢 Hangman Game

A simple command-line Hangman game built with Python.  
Guess the hidden word letter by letter before you run out of attempts.

## 📌 Description

The program:

- Randomly selects a word from a predefined list
- Lets the user guess one letter at a time
- Tracks guessed letters and remaining attempts
- Displays the current state of the word (e.g. `p _ t _ o n`)
- Ends when the user wins or runs out of attempts

This project practices strings, loops, conditionals, sets, and the `random` module.

## ✨ Features

- 🎯 Random word selection  
- 🔤 Single-letter input validation  
- 🧠 Tracks guessed letters  
- ❤️ Limited attempts (6)  
- 🏆 Win / lose messages  

## 🛠️ Technologies Used

- Python 3  
- Built-in `random` module  

## 🚀 How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Run the game:
   ```bash
   python 17_Hangman.py
   ```

## 🧪 Sample Output

```text
Welcome to Hangman!

Word: ______
Attempts left: 6
Guessed letters: 
Enter a letter: p

Word: p_____
Attempts left: 6
Guessed letters: p
Enter a letter: z

Word: p_____
Attempts left: 5
Guessed letters: p z
Wrong guess!
```

## 👨‍💻 Author

**Athul Sathyan**
