import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = {"phone": phone}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"👤 {name} | 📞 {info['phone']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\n👤 {name}\n📞 {info['phone']}\n")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# --- Main Menu ---

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
