from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class ContactBook(Widget):
    contacts = Reactive([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = ""
        self.search_results = []

    def render(self):
        contact_list = "\n".join([f"{contact['name']}: {contact['number']}" for contact in self.contacts])
        return Vertical(
            Static("Contact Book"),
            Static(self.message),
            Static(contact_list if contact_list else "No contacts available."),
            Button(label="Add Contact", id="add"),
            Button(label="Remove Contact", id="remove"),
            Button(label="Search Contact", id="search"),
            Button(label="List Contacts", id="list"),
            Static("\n".join(self.search_results)),
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_contact()
        elif button_id == "remove":
            await self.remove_contact()
        elif button_id == "search":
            await self.search_contact()
        elif button_id == "list":
            await self.list_contacts()
        await self.refresh()

    async def add_contact(self):
        self.message = "Enter contact name and number separated by a comma:"
        await self.refresh()
        name_number = await self.ask_user_input()
        if name_number:
            name, number = name_number.split(",")
            self.contacts.append({"name": name.strip(), "number": number.strip()})
            self.message = f"Added contact: {name.strip()}"

    async def remove_contact(self):
        self.message = "Enter contact name to remove:"
        await self.refresh()
        name = await self.ask_user_input()
        self.contacts = [contact for contact in self.contacts if contact["name"] != name.strip()]
        self.message = f"Removed contact: {name.strip()}"

    async def search_contact(self):
        self.message = "Enter contact name to search:"
        await self.refresh()
        name = await self.ask_user_input()
        results = [contact for contact in self.contacts if name.strip().lower() in contact["name"].lower()]
        self.search_results = [f"{contact['name']}: {contact['number']}" for contact in results]
        self.message = f"Search results for '{name.strip()}':" if results else f"No contact found for '{name.strip()}'"

    async def list_contacts(self):
        self.search_results = [f"{contact['name']}: {contact['number']}" for contact in self.contacts]
        self.message = "Listing all contacts:"

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

class ContactBookApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.book = ContactBook()
        await self.view.dock(self.book)

if __name__ == "__main__":
    app = ContactBookApp()
    app.run()
