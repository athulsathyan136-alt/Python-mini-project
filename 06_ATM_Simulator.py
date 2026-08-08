balance = 10000
pin = "9961"

user_pin = input("Enter PIN: ")

if user_pin == pin:
    print("Login successful!")

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = input("Choose option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        balance += amount
        print("New balance:", balance)

    elif choice == "3":
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("New balance:", balance)
        else:
            print("Insufficient balance")

    else:
        print("Invalid option")

else:
    print("Wrong PIN")