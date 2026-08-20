contacts = {}

while True:
    print("\n============= Contact Book =============")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        if contacts:
            print("\nContact List")

            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif choice == "3":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 5.")