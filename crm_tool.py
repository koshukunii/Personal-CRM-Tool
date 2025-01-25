import json

# File where contacts will be saved
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts


def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully!")
    else:
        print("Contact not found.")


def main():
    """Main function to interact with the CRM tool."""
    contacts = load_contacts()

    while True:
        print("\nCRM Tool - Choose an option:")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Delete a Contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting the CRM Tool. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
