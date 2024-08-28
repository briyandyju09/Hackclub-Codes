import json
import os

class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)
        self.load()

    def load(self):
        with open(self.filename, "r") as f:
            self.items = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.items, f, indent=4)

    def add_item(self, name, quantity, price):
        if name in self.items:
            print(f"Item '{name}' already exists. Use update to change quantity.")
            return
        self.items[name] = {"quantity": quantity, "price": price}
        self.save()
        print(f"Added item '{name}' with quantity {quantity} and price ${price:.2f}.")

    def remove_item(self, name):
        if name not in self.items:
            print(f"Item '{name}' not found.")
            return
        del self.items[name]
        self.save()
        print(f"Removed item '{name}'.")

    def update_quantity(self, name, quantity):
        if name not in self.items:
            print(f"Item '{name}' not found.")
            return
        self.items[name]["quantity"] = quantity
        self.save()
        print(f"Updated item '{name}' to quantity {quantity}.")

    def update_price(self, name, price):
        if name not in self.items:
            print(f"Item '{name}' not found.")
            return
        self.items[name]["price"] = price
        self.save()
        print(f"Updated item '{name}' to price ${price:.2f}.")

    def view_inventory(self):
        if not self.items:
            print("No items in inventory.")
            return
        for name, details in self.items.items():
            print(f"Item: {name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def main():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. View Inventory")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_item(name, quantity, price)

        elif choice == "2":
            name = input("Enter item name: ")
            inventory.remove_item(name)

        elif choice == "3":
            name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(name, quantity)

        elif choice == "4":
            name = input("Enter item name: ")
            price = float(input("Enter new price: "))
            inventory.update_price(name, price)

        elif choice == "5":
            inventory.view_inventory()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
