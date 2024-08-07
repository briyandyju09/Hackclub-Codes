from textual.app import App
from textual.widget import Widget
from textual.containers import Vertical
from textual.widgets import Static, Button, Input
import random

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_health = 100
        self.enemy_health = 100
        self.inventory = []
        self.quest_completed = False
        self.text_log = []

    def render(self):
        return Vertical(
            Static(f"Player Health: {self.player_health}"),
            Static(f"Enemy Health: {self.enemy_health}"),
            Static(f"Inventory: {', '.join(self.inventory)}"),
            Static("\n".join(self.text_log)),
            Button(label="Attack", name="attack"),
            Button(label="Heal", name="heal"),
            Button(label="Explore", name="explore"),
            Button(label="Check Quest", name="quest"),
        )

    async def on_button_pressed(self, event):
        if event.button.name == "attack":
            self.attack_enemy()
        elif event.button.name == "heal":
            self.heal_player()
        elif event.button.name == "explore":
            self.explore()
        elif event.button.name == "quest":
            self.check_quest()
        await self.refresh()

    def attack_enemy(self):
        damage = random.randint(10, 30)
        self.enemy_health -= damage
        self.text_log.append(f"You attacked the enemy for {damage} damage.")
        if self.enemy_health <= 0:
            self.text_log.append("You defeated the enemy!")
            self.enemy_health = 0
            if not self.quest_completed:
                self.inventory.append("Quest Item")
                self.text_log.append("You found a quest item!")
                self.quest_completed = True
        else:
            self.enemy_counter_attack()

    def enemy_counter_attack(self):
        damage = random.randint(5, 20)
        self.player_health -= damage
        self.text_log.append(f"The enemy attacked you for {damage} damage.")
        if self.player_health <= 0:
            self.text_log.append("You have been defeated!")
            self.player_health = 0

    def heal_player(self):
        heal_amount = random.randint(10, 30)
        self.player_health += heal_amount
        if self.player_health > 100:
            self.player_health = 100
        self.text_log.append(f"You healed yourself for {heal_amount} health.")

    def explore(self):
        event = random.choice(["You found a potion!", "You encountered an enemy!"])
        if event == "You encountered an enemy!":
            self.enemy_health = random.randint(50, 100)
            self.text_log.append("An enemy has appeared!")
        else:
            self.inventory.append("Potion")
            self.text_log.append("You found a potion and added it to your inventory.")

    def check_quest(self):
        if self.quest_completed:
            self.text_log.append("You have completed the quest and obtained a quest item!")
        else:
            self.text_log.append("You have not completed the quest yet.")

class TextAdventureApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event):
        self.game = Game()
        await self.view.dock(self.game)

if __name__ == "__main__":
    TextAdventureApp.run()
