import sqlite3
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel

console = Console()
db_path = 'appointments.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            appointment_date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_appointment():
    title = Prompt.ask("Enter the appointment title")
    description = Prompt.ask("Enter the appointment description (optional)", default="")
    appointment_date = Prompt.ask("Enter the appointment date (YYYY-MM-DD HH:MM:SS)")
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (title, description, appointment_date, created_at)
        VALUES (?, ?, ?, ?)
    ''', (title, description, appointment_date, created_at))
    conn.commit()
    conn.close()

    console.print(Panel("Appointment added successfully!", style="green"))

def view_appointments():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, appointment_date, created_at FROM appointments')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print(Panel("No appointments found.", style="red"))
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Title", min_width=20)
    table.add_column("Description", min_width=30)
    table.add_column("Date", min_width=20)
    table.add_column("Created At", min_width=20)

    for row in rows:
        table.add_row(str(row[0]), row[1], row[2], row[3], row[4])

    console.print(table)

def update_appointment():
    appointment_id = int(Prompt.ask("Enter the appointment ID to update"))
    title = Prompt.ask("Enter the new title (leave blank to keep current)")
    description = Prompt.ask("Enter the new description (leave blank to keep current)")
    appointment_date = Prompt.ask("Enter the new date (YYYY-MM-DD HH:MM:SS, leave blank to keep current)")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if title:
        cursor.execute('UPDATE appointments SET title = ? WHERE id = ?', (title, appointment_id))
    if description:
        cursor.execute('UPDATE appointments SET description = ? WHERE id = ?', (description, appointment_id))
    if appointment_date:
        cursor.execute('UPDATE appointments SET appointment_date = ? WHERE id = ?', (appointment_date, appointment_id))
    
    conn.commit()
    conn.close()

    console.print(Panel("Appointment updated successfully!", style="green"))

def delete_appointment():
    appointment_id = int(Prompt.ask("Enter the appointment ID to delete"))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()

    console.print(Panel("Appointment deleted successfully!", style="green"))

def main():
    init_db()
    while True:
        console.print(Panel("Appointment Scheduler", style="bold blue", title="Menu", title_align="left"))
        option = Prompt.ask("Choose an option: [1] Add Appointment, [2] View Appointments, [3] Update Appointment, [4] Delete Appointment, [5] Exit", choices=["1", "2", "3", "4", "5"], default="5")

        if option == "1":
            add_appointment()
        elif option == "2":
            view_appointments()
        elif option == "3":
            update_appointment()
        elif option == "4":
            delete_appointment()
        elif option == "5":
            console.print(Panel("Goodbye!", style="bold green"))
            break

if __name__ == "__main__":
    main()
