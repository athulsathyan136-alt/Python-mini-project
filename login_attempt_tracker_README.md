# 🔐 Login Attempt Tracker

A simple Python login system that allows a user to log in with a username and password. The account is locked after three failed login attempts.

## 🚀 Features

- Username and password validation
- Maximum 3 login attempts
- Displays remaining attempts
- Locks the account after failed attempts
- Beginner-friendly Python project

## 🛠️ Technologies

- Python 3

## 📁 Project Structure

```text
python-login-attempt-tracker/
│
├── 21_login_attempt_tracker.py
└── README.md

💡 Example
===== LOGIN SYSTEM =====

Username: admin
Password: 1234

❌ Incorrect password.
Attempts remaining: 2

Username: admin
Password: admin123

✅ Login successful!
Welcome, admin!

After three failed attempts:

❌ Incorrect password.
❌ Incorrect password.
❌ Incorrect password.

🔒 Account locked due to too many failed attempts.

Disclaimer

This project is designed for educational purposes. It does not implement production-level security features such as password hashing, encryption, databases, rate limiting, or multi-factor authentication.

👨‍💻 Author

Athul Sathyan

GitHub: athulsathyan136-alt
