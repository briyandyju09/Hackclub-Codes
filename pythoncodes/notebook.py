import sqlite3
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel

console = Console()
db_path = 'notes.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_note():
    title = Prompt.ask("Enter the note title")
    content = Prompt.ask("Enter the note content (optional)", default="")
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notes (title, content, created_at)
        VALUES (?, ?, ?)
    ''', (title, content, created_at))
    conn.commit()
    conn.close()

    console.print(Panel("Note created successfully!", style="green"))

def view_notes():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, created_at FROM notes')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print(Panel("No notes found.", style="red"))
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", min_width=20)
    table.add_column("Created At", min_width=20)

    for row in rows:
        table.add_row(str(row[0]), row[1], row[2])

    console.print(table)

def view_note_detail(note_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content, created_at FROM notes WHERE id = ?', (note_id,))
    note = cursor.fetchone()
    conn.close()

    if note:
        title, content, created_at = note
        console.print(Panel(f"[bold]Title:[/bold] {title}\n\n[bold]Content:[/bold] {content}\n\n[bold]Created At:[/bold] {created_at}", style="cyan"))
    else:
        console.print(Panel("Note not found.", style="red"))

def edit_note():
    note_id = int(Prompt.ask("Enter the note ID to edit"))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content FROM notes WHERE id = ?', (note_id,))
    note = cursor.fetchone()

    if note:
        title = Prompt.ask("Enter the new title", default=note[0])
        content = Prompt.ask("Enter the new content", default=note[1])
        cursor.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
        conn.commit()
        console.print(Panel("Note updated successfully!", style="green"))
    else:
        console.print(Panel("Note not found.", style="red"))

    conn.close()

def delete_note():
    note_id = int(Prompt.ask("Enter the note ID to delete"))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()

    console.print(Panel("Note deleted successfully!", style="green"))

def search_notes():
    keyword = Prompt.ask("Enter a keyword to search for in the notes")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, created_at FROM notes WHERE title LIKE ? OR content LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print(Panel("No notes found matching your search.", style="red"))
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", min_width=20)
    table.add_column("Created At", min_width=20)

    for row in rows:
        table.add_row(str(row[0]), row[1], row[2])

    console.print(table)

def main():
    init_db()
    while True:
        console.print(Panel("Note-Taking Application", style="bold blue", title="Menu", title_align="left"))
        option = Prompt.ask("Choose an option: [1] Create Note, [2] View Notes, [3] Edit Note, [4] Delete Note, [5] Search Notes, [6] Exit", choices=["1", "2", "3", "4", "5", "6"], default="6")

        if option == "1":
            create_note()
        elif option == "2":
            view_notes()
            note_id = Prompt.ask("Enter the note ID to view details or press Enter to go back", default="")
            if note_id.isdigit():
                view_note_detail(int(note_id))
        elif option == "3":
            edit_note()
        elif option == "4":
            delete_note()
        elif option == "5":
            search_notes()
        elif option == "6":
            console.print(Panel("Goodbye!", style="bold green"))
            break

if __name__ == "__main__":
    main()
