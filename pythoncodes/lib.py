class Book:
    def __init__(self, title, author, genre, is_available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nStatus: {status}\n"

class Library:
    def __init__(self):
        self.books = []
        self.run()

    def add_book(self):
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()
        genre = input("Enter the genre: ").strip()
        self.books.append(Book(title, author, genre))
        print(f"Added book: {title}")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")

    def update_book(self):
        self.view_books()
        if not self.books:
            return

        try:
            index = int(input("Enter the number of the book to update: ")) - 1
            if 0 <= index < len(self.books):
                book = self.books[index]
                book.title = input(f"Enter new title (current: {book.title}): ").strip()
                book.author = input(f"Enter new author (current: {book.author}): ").strip()
                book.genre = input(f"Enter new genre (current: {book.genre}): ").strip()
                status_input = input(f"Is the book available? (yes/no) (current: {'yes' if book.is_available else 'no'}): ").strip().lower()
                book.is_available = status_input in ['yes', 'y']
                print(f"Updated book: {book.title}")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_book(self):
        self.view_books()
        if not self.books:
            return

        try:
            index = int(input("Enter the number of the book to delete: ")) - 1
            if 0 <= index < len(self.books):
                deleted_book = self.books.pop(index)
                print(f"Deleted book: {deleted_book.title}")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_books(self):
        search_term = input("Enter the title or author to search: ").strip().lower()
        found_books = [book for book in self.books if search_term in book.title.lower() or search_term in book.author.lower()]
        
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(book)
        else:
            print("No books found.")

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Search Books")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                self.update_book()
            elif choice == '4':
                self.delete_book()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    Library()