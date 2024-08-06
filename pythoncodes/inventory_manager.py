import logging
from datetime import datetime


LOG_FILE = 'inventory_manager.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


inventory = []


def add_item(item_name, quantity, price):
    item = {'name': item_name, 'quantity': quantity, 'price': price}
    inventory.append(item)
    logging.info(f"Added item: {item}")


def remove_item(item_name):
    global inventory
    inventory = [item for item in inventory if item['name'] != item_name]
    logging.info(f"Removed item: {item_name}")


def list_items():
    if inventory:
        logging.info("Listing all items")
        for idx, item in enumerate(inventory, start=1):
            print(f"{idx}. Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
            logging.info(f"Item {idx}: {item}")
    else:
        logging.info("No items in the inventory")
        print("Your inventory is empty.")


def summary_report():
    total_value = sum(item['quantity'] * item['price'] for item in inventory)
    total_items = sum(item['quantity'] for item in inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Total value of inventory: ${total_value:.2f}")
    logging.info(f"Generated summary report: Total items - {total_items}, Total value - ${total_value:.2f}")


def main():
    print("Welcome to the Simple Inventory Management System!")
    logging.info("Started Inventory Management System")
    
    while True:
        print("\nOptions:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. List all items")
        print("4. Generate summary report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                add_item(item_name, quantity, price)
            except ValueError:
                print("Please enter valid quantity and price.")
        elif choice == '2':
            item_name = input("Enter item name to remove: ")
            remove_item(item_name)
        elif choice == '3':
            list_items()
        elif choice == '4':
            summary_report()
        elif choice == '5':
            logging.info("Exiting Inventory Management System")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()


def setup_notification_system():
    logging.info("Setting up notification system")
    pass

def check_system_status():
    logging.info("Checking system status")
    pass


setup_notification_system()
check_system_status()

def display_welcome_message():
    print("Welcome to the Simple Inventory Management System!")
    print("You can add, remove, and list items.")
    print("You can also generate a summary report of your inventory.")


display_welcome_message()
logging.info("Displayed welcome message")
