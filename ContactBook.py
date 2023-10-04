
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for idx, contact in enumerate(self.contacts):
            print(f"{idx + 1}. {contact.name}: {contact.phone_number}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.name or query in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("Contact updated successfully.")
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid index.")

# Initialize the contact manager
contact_manager = ContactManager()
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        contact = Contact(name, phone_number, email, address)
        contact_manager.add_contact(contact)
        print("Contact added successfully.")

    elif choice == "2":
        contact_manager.view_contact_list()

    elif choice == "3":
        query = input("Enter the name or phone number to search: ")
        results = contact_manager.search_contact(query)
        if results:
            print("Search results:")
            for idx, contact in enumerate(results):
                print(f"{idx + 1}. {contact.name}: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    elif choice == "4":
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contact_manager.contacts):
            name = input("Enter the new name: ")
            phone_number = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            updated_contact = Contact(name, phone_number, email, address)
            contact_manager.update_contact(index, updated_contact)
        else:
            print("Invalid index.")

    elif choice == "5":
        index = int(input("Enter the index of the contact to delete: ")) - 1
        contact_manager.delete_contact(index)

    elif choice == "6":
        print("Exiting the Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
