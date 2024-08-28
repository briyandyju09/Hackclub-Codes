import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}"

class Room:
    def __init__(self, description, enemy=None, item=None):
        self.description = description
        self.enemy = enemy
        self.item = item

    def enter(self):
        print(self.description)
        if self.enemy:
            print(f"You encounter a {self.enemy.name}!")
            return "battle"
        elif self.item:
            print(f"You find a {self.item}!")
            return "item"
        return "empty"

class RPGGame:
    def __init__(self):
        self.player = Character("Hero", 100, 20)
        self.rooms = [
            Room("A dark, damp cave.", Character("Goblin", 30, 10)),
            Room("A sunny meadow with flowers.", item="Magic Sword"),
            Room("An eerie forest with strange noises.", Character("Orc", 50, 15)),
            Room("A cozy cabin with a warm fire.", item="Healing Potion")
        ]
        self.current_room = 0

    def move(self):
        room = self.rooms[self.current_room]
        result = room.enter()

        if result == "battle":
            enemy = room.enemy
            while self.player.is_alive() and enemy.is_alive():
                self.player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_enemy(self.player)
                if not self.player.is_alive():
                    print("You have been defeated. Game Over.")
                    return False
            print(f"You defeated the {enemy.name}!")
        elif result == "item":
            print(f"You picked up a {room.item}.")
        self.current_room += 1
        if self.current_room >= len(self.rooms):
            print("You have explored all rooms. Congratulations!")
            return False
        return True

    def play(self):
        while self.player.is_alive() and self.current_room < len(self.rooms):
            print("\nCurrent Room:")
            if not self.move():
                break
            print(f"\n{self.player}")
        print("\nGame Over")

def main():
    game = RPGGame()
    game.play()

if __name__ == "__main__":
    main()
