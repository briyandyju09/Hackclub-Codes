import os

class TextEditor:
    def __init__(self):
        self.filename = None
        self.content = ""
        self.run()

    def create_file(self):
        self.filename = input("Enter new file name: ").strip()
        if os.path.exists(self.filename):
            print("File already exists. Opening the existing file.")
            self.open_file(self.filename)
        else:
            self.content = ""
            print(f"Created new file: {self.filename}")

    def open_file(self, filename=None):
        if not filename:
            self.filename = input("Enter file name to open: ").strip()
        else:
            self.filename = filename

        if not os.path.exists(self.filename):
            print("File not found.")
        else:
            with open(self.filename, 'r') as file:
                self.content = file.read()
            print(f"Opened file: {self.filename}")

    def save_file(self):
        if not self.filename:
            self.filename = input("Enter file name to save: ").strip()
        with open(self.filename, 'w') as file:
            file.write(self.content)
        print(f"Saved file: {self.filename}")

    def edit_file(self):
        if not self.filename:
            print("No file is currently open. Please create or open a file first.")
            return
        print("Enter text (type 'SAVE' on a new line to save changes):")
        lines = []
        while True:
            line = input()
            if line == 'SAVE':
                break
            lines.append(line)
        self.content = '\n'.join(lines)
        self.save_file()

    def view_file(self):
        if not self.filename:
            print("No file is currently open. Please create or open a file first.")
        else:
            print(f"Content of {self.filename}:")
            print(self.content)

    def run(self):
        while True:
            print("\nText Editor")
            print("1. Create File")
            print("2. Open File")
            print("3. Edit File")
            print("4. View File")
            print("5. Save File")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.create_file()
            elif choice == '2':
                self.open_file()
            elif choice == '3':
                self.edit_file()
            elif choice == '4':
                self.view_file()
            elif choice == '5':
                self.save_file()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    TextEditor()