import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()
        self.run()

    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error loading contacts file. File may be corrupted.")
                return {}
        return {}

    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except IOError:
            print("Error saving contacts to file.")

    def add_contact(self, name, phone):
        if not name or not phone:
            print("Name and phone number cannot be empty.")
            return
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = phone
            self.save_contacts()
            print(f"Added contact: {name}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Deleted contact: {name}")
        else:
            print("Contact not found.")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            self.save_contacts()
            print(f"Updated contact: {name}")
        else:
            print("Contact not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")

    def run(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Update Contact")
            print("4. View Contacts")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                name = input("Enter contact name: ").strip()
                phone = input("Enter contact phone number: ").strip()
                self.add_contact(name, phone)
            elif choice == '2':
                name = input("Enter contact name to delete: ").strip()
                self.delete_contact(name)
            elif choice == '3':
                name = input("Enter contact name to update: ").strip()
                if name in self.contacts:
                    new_phone = input("Enter new phone number: ").strip()
                    self.update_contact(name, new_phone)
                else:
                    print("Contact not found.")
            elif choice == '4':
                self.view_contacts()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    ContactManager()