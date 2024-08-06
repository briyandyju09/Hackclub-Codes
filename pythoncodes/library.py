import json
import os

class LibraryManager:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()
        self.run()

    def load_books(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error loading library file. File may be corrupted.")
                return []
        return []

    def save_books(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.books, file, indent=4)
        except IOError:
            print("Error saving library to file.")

    def add_book(self, title, author):
        if not title or not author:
            print("Title and author cannot be empty.")
            return
        for book in self.books:
            if book['title'] == title:
                print("Book already exists.")
                return
        self.books.append({'title': title, 'author': author})
        self.save_books()
        print(f"Added book: {title} by {author}")

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                self.save_books()
                print(f"Removed book: {title}")
                return
        print("Book not found.")

    def update_book(self, title, new_title, new_author):
        for book in self.books:
            if book['title'] == title:
                book['title'] = new_title if new_title else book['title']
                book['author'] = new_author if new_author else book['author']
                self.save_books()
                print(f"Updated book: {title}")
                return
        print("Book not found.")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}")

    def run(self):
        while True:
            print("\nLibrary Manager")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Update Book")
            print("4. View Books")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                self.add_book(title, author)
            elif choice == '2':
                title = input("Enter book title to remove: ").strip()
                self.remove_book(title)
            elif choice == '3':
                title = input("Enter book title to update: ").strip()
                if any(book['title'] == title for book in self.books):
                    new_title = input("Enter new title (leave empty to keep current): ").strip()
                    new_author = input("Enter new author (leave empty to keep current): ").strip()
                    self.update_book(title, new_title, new_author)
                else:
                    print("Book not found.")
            elif choice == '4':
                self.view_books()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    LibraryManager()