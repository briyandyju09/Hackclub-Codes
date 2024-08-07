from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
from textual.reactive import Reactive

class Store(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = {}
        self.message = ""
        self.search_results = []

    def render(self):
        return Vertical(
            Static("Store Inventory Management System"),
            Button(label="Add Product", id="add"),
            Button(label="Remove Product", id="remove"),
            Button(label="List Products", id="list"),
            Button(label="Search Product", id="search"),
            Static(self.message),
            Static("\n".join(self.search_results))
        )

    async def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "add":
            await self.add_product()
        elif button_id == "remove":
            await self.remove_product()
        elif button_id == "list":
            await self.list_products()
        elif button_id == "search":
            await self.search_product()
        await self.refresh()

    async def add_product(self):
        self.message = "Enter product name and quantity separated by a comma:"
        await self.refresh()
        name_quantity = await self.ask_user_input()
        if name_quantity:
            name, quantity = name_quantity.split(",")
            self.inventory[name.strip()] = int(quantity.strip())
            self.message = f"Added {quantity.strip()} of {name.strip()}"

    async def remove_product(self):
        self.message = "Enter product name to remove:"
        await self.refresh()
        name = await self.ask_user_input()
        if name in self.inventory:
            del self.inventory[name.strip()]
            self.message = f"Removed {name.strip()}"
        else:
            self.message = f"Product {name.strip()} not found"

    async def list_products(self):
        self.search_results = [f"{name}: {quantity}" for name, quantity in self.inventory.items()]
        self.message = "Listing all products:"

    async def search_product(self):
        self.message = "Enter product name to search:"
        await self.refresh()
        name = await self.ask_user_input()
        if name in self.inventory:
            self.search_results = [f"{name.strip()}: {self.inventory[name.strip()]}"]
            self.message = f"Product found:"
        else:
            self.search_results = []
            self.message = f"Product {name.strip()} not found"

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

class InventoryApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")

    async def on_mount(self, event):
        self.store = Store()
        await self.view.dock(self.store)

if __name__ == "__main__":
    app = InventoryApp()
    app.run()