class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.connections = {}

  
    def connect(self, direction, room):
        self.connections[direction] = room

  
    def get_description(self):
        return f"{self.name}\n{self.description}\nItems: {', '.join(self.items)}\n"


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms['Living Room']
        self.inventory = []

  
    def create_rooms(self):
        living_room = Room("Living Room", "A cozy room with a couch and a TV.")
        kitchen = Room("Kitchen", "A room with a fridge and a stove.", ["apple"])
        bedroom = Room("Bedroom", "A small room with a bed and a wardrobe.", ["key"])
        bathroom = Room("Bathroom", "A clean room with a shower and a toilet.")

        living_room.connect("north", kitchen)
        living_room.connect("east", bedroom)
        kitchen.connect("south", living_room)
        bedroom.connect("west", living_room)
        bedroom.connect("north", bathroom)
        bathroom.connect("south", bedroom)

        return {
            "Living Room": living_room,
            "Kitchen": kitchen,
            "Bedroom": bedroom,
            "Bathroom": bathroom
        }

  
    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            print(f"You moved to the {self.current_room.name}.")
        else:
            print("You can't go that way.")

  
    def pick_up(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print("That item is not here.")

  
    def show_inventory(self):
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'empty'}")

  
    def play(self):
        while True:
            print(self.current_room.get_description())
            command = input("Enter a command (move [direction], pick up [item], inventory, exit): ").strip().split()
            if not command:
                continue
            action = command[0].lower()
            if action == "move":
                if len(command) > 1:
                    self.move(command[1].lower())
                else:
                    print("Move where?")
            elif action == "pick":
                if len(command) > 2 and command[1].lower() == "up":
                    self.pick_up(command[2].lower())
                else:
                    print("Pick up what?")
            elif action == "inventory":
                self.show_inventory()
            elif action == "exit":
                print("Goodbye!")
                break
            else:
                print("Unknown command.")


if __name__ == '__main__':
    game = Game()
    game.play()
