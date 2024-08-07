from datetime import datetime

class JournalEntry:
    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nDate: {self.date}\nContent:\n{self.content}\n"

class JournalManager:
    def __init__(self):
        self.entries = []
        self.run()

    def add_entry(self):
        title = input("Enter the title of the entry: ").strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = input("Enter the content of the entry: ").strip()
        entry = JournalEntry(title, date, content)
        self.entries.append(entry)
        print(f"Added entry: {title}")

    def view_entries(self):
        if not self.entries:
            print("No entries available.")
        else:
            for i, entry in enumerate(self.entries):
                print(f"Entry {i + 1}:")
                print(entry)

    def update_entry(self):
        self.view_entries()
        if not self.entries:
            return
        try:
            index = int(input("Enter the number of the entry to update: ")) - 1
            if 0 <= index < len(self.entries):
                entry = self.entries[index]
                entry.title = input(f"Enter new title (current: {entry.title}): ").strip()
                entry.content = input(f"Enter new content (current: {entry.content}): ").strip()
                entry.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update the date to current time
                print(f"Updated entry: {entry.title}")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_entry(self):
        self.view_entries()
        if not self.entries:
            return
        try:
            index = int(input("Enter the number of the entry to delete: ")) - 1
            if 0 <= index < len(self.entries):
                entry = self.entries.pop(index)
                print(f"Deleted entry: {entry.title}")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_entries(self):
        keyword = input("Enter a keyword to search for: ").strip().lower()
        found = False
        for entry in self.entries:
            if (keyword in entry.title.lower()) or (keyword in entry.content.lower()):
                print(entry)
                found = True
        if not found:
            print("No entries found with that keyword.")

    def run(self):
        while True:
            print("\nJournal Manager")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Update Entry")
            print("4. Delete Entry")
            print("5. Search Entries")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.view_entries()
            elif choice == '3':
                self.update_entry()
            elif choice == '4':
                self.delete_entry()
            elif choice == '5':
                self.search_entries()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    JournalManager()
