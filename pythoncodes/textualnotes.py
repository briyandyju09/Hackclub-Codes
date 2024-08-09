from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class NoteTakingApp(Widget):
    notes = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.current_note = ""

    def render(self):
        note_list = "\n".join([f"{idx + 1}. {note['title']}" for idx, note in enumerate(self.notes)])
        return Vertical(
            Static("Note Taking App"),
            Static(self.message),
            Static(note_list if note_list else "No notes available."),
            Button(label="Add Note", id="add"),
            Button(label="View Note", id="view"),
            Button(label="Delete Note", id="delete"),
            Button(label="Search Notes", id="search"),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_note()
        elif button_id == "view":
            await self.view_note()
        elif button_id == "delete":
            await self.delete_note()
        elif button_id == "search":
            await self.search_notes()
        await self.refresh()

    async def add_note(self):
        self.message = "Enter the note title and content separated by a comma:"
        await self.refresh()
        title_content = await self.ask_user_input()
        if title_content:
            title, content = title_content.split(",", 1)
            self.notes.append({"title": title.strip(), "content": content.strip()})
            self.message = f"Added note: {title.strip()}"

    async def view_note(self):
        self.message = "Enter the note title to view:"
        await self.refresh()
        title = await self.ask_user_input()
        for note in self.notes:
            if note["title"] == title.strip():
                self.current_note = note["content"]
                self.message = f"Viewing note: {note['title']}\n{self.current_note}"
                break
        else:
            self.message = f"Note '{title.strip()}' not found."

    async def delete_note(self):
        self.message = "Enter the note title to delete:"
        await self.refresh()
        title = await self.ask_user_input()
        self.notes = [note for note in self.notes if note["title"] != title.strip()]
        self.message = f"Deleted note: {title.strip()}"

    async def search_notes(self):
        self.message = "Enter a keyword to search notes:"
        await self.refresh()
        keyword = await self.ask_user_input()
        matching_notes = [note for note in self.notes if keyword.strip().lower() in note["title"].lower() or keyword.strip().lower() in note["content"].lower()]
        if matching_notes:
            self.current_note = "\n".join([f"{note['title']}: {note['content']}" for note in matching_notes])
            self.message = f"Found {len(matching_notes)} matching note{'s' if len(matching_notes) > 1 else ''}:\n{self.current_note}"
        else:
            self.message = "No matching notes found."

    async def ask_user_input(self):
        input_widget = Input()
        await self.view.dock(input_widget)
        input_widget.focus()
        await self.wait_for_input(input_widget)
        user_input = input_widget.value
        await input_widget.remove()
        return user_input

    async def wait_for_input(self, input_widget):
        while not input_widget.value:
            await self.sleep(0.1)

class SimpleNoteApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.notetaker = NoteTakingApp()
        await self.view.dock(self.notetaker)

if __name__ == "__main__":
    app = SimpleNoteApp()
    app.run()
