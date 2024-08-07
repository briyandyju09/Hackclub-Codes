class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        ingredients = ', '.join(self.ingredients)
        return f"Recipe: {self.name}\nIngredients: {ingredients}\nInstructions: {self.instructions}"

class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.run()

    def add_recipe(self):
        name = input("Enter recipe name: ").strip()
        ingredients = input("Enter ingredients (comma-separated): ").strip().split(',')
        ingredients = [ingredient.strip() for ingredient in ingredients]
        instructions = input("Enter cooking instructions: ").strip()
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
        print(f"Added recipe: {recipe.name}")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes available.")
        else:
            for i, recipe in enumerate(self.recipes):
                print(f"{i+1}. {recipe}")

    def update_recipe(self):
        self.view_recipes()
        if not self.recipes:
            return
        try:
            index = int(input("Enter the number of the recipe to update: ")) - 1
            if 0 <= index < len(self.recipes):
                recipe = self.recipes[index]
                recipe.name = input(f"Enter new name (current: {recipe.name}): ").strip()
                ingredients = input("Enter new ingredients (comma-separated): ").strip().split(',')
                recipe.ingredients = [ingredient.strip() for ingredient in ingredients]
                recipe.instructions = input(f"Enter new instructions (current: {recipe.instructions}): ").strip()
                print(f"Updated recipe: {recipe.name}")
            else:
                print("Invalid recipe number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_recipe(self):
        self.view_recipes()
        if not self.recipes:
            return
        try:
            index = int(input("Enter the number of the recipe to delete: ")) - 1
            if 0 <= index < len(self.recipes):
                recipe = self.recipes.pop(index)
                print(f"Deleted recipe: {recipe.name}")
            else:
                print("Invalid recipe number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_by_ingredient(self):
        ingredient = input("Enter ingredient to search for: ").strip()
        found = False
        for recipe in self.recipes:
            if ingredient in recipe.ingredients:
                print(recipe)
                found = True
        if not found:
            print("No recipes found with that ingredient.")

    def run(self):
        while True:
            print("\nRecipe Manager")
            print("1. Add Recipe")
            print("2. View Recipes")
            print("3. Update Recipe")
            print("4. Delete Recipe")
            print("5. Search by Ingredient")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_recipe()
            elif choice == '2':
                self.view_recipes()
            elif choice == '3':
                self.update_recipe()
            elif choice == '4':
                self.delete_recipe()
            elif choice == '5':
                self.search_by_ingredient()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    RecipeManager()