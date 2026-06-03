# CONTACT BOOK
import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

contacts = load_contacts()

def save_contact():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# This creates an empty dictionary called contacts. Stores Key-value pairs. Name = Key; Details = phone, email


# This function  is responsible for adding a new contact
def add_contact():
    # .strip() removes extra spaces from the beginning and end.
    name = input("Enter your name: ").strip()

    # This checks if the name already exists in the contacts dictionary.
    if name in contacts:
        print("Contact already exists")
        return

    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email address: ").strip()

    # This adds the new contact to the dictionary.
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added.")

# This defines a function that displays all saved contacts.
def view_contacts():
    # In Python, an empty dictionary counts as False.
    if not contacts:
        print("Contact does not exist")
        return

    print("\nContact list:")
    # .items() gives both the key and value.
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")

# This defines a function for searching contacts by keywords.
def search_contact():
    # .strip() - removes extra spaces and .lower() converts the text to lowercase
    search_text = input("Enter contact name to search: ").strip().lower()

    # This creates an empty list. This list will store every matching contact.
    found_contacts = []
    for name, details in contacts.items():
        if search_text in name.lower():
            # (name, details) is a tuple containing the contact name and contact details.
            found_contacts.append((name, details))

    if found_contacts:
        print("\nMatching contacts:")

        # This loops through only the contacts that matched the search.
        for name, details in found_contacts:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("No matching contacts found")

# This defines a function for updating an existing contact.
def update_contact():
    name_to_update = input("Enter the name of the contact that you want to update: ").strip()
    if name_to_update not in contacts:
        print("Contact not found")
        return
    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()
    contacts[name_to_update]["phone"] = phone
    contacts[name_to_update]["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    name_to_delete = input("Enter the name of the contact that you want to delete: ").strip()

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        save_contact()
        print("Contact deleted successfully.")
    else:
        print("Contact not found")

def show_menu():
    print("\nContact Book Menu")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Save contact")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter the number that matches your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            save_contact()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()
