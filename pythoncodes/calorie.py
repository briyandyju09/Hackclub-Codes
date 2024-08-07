from datetime import datetime

class Meal:
    def __init__(self, name, calories, date):
        self.name = name
        self.calories = calories
        self.date = date

    def __str__(self):
        return f"Meal: {self.name}, Calories: {self.calories}, Date: {self.date}"

class CalorieTracker:
    def __init__(self):
        self.meals = []
        self.run()

    def add_meal(self):
        name = input("Enter the name of the meal: ").strip()
        try:
            calories = int(input("Enter the number of calories: ").strip())
        except ValueError:
            print("Invalid calorie input. Please enter a number.")
            return
        date = input("Enter the date of the meal (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        meal = Meal(name, calories, date)
        self.meals.append(meal)
        print(f"Added meal: {meal}")

    def view_meals(self):
        if not self.meals:
            print("No meals available.")
        else:
            for meal in self.meals:
                print(meal)

    def update_meal(self):
        self.view_meals()
        if not self.meals:
            return
        try:
            index = int(input("Enter the number of the meal to update: ")) - 1
            if 0 <= index < len(self.meals):
                meal = self.meals[index]
                meal.name = input(f"Enter new name (current: {meal.name}): ").strip()
                try:
                    meal.calories = int(input(f"Enter new calorie count (current: {meal.calories}): ").strip())
                except ValueError:
                    print("Invalid calorie input. Please enter a number.")
                    return
                meal.date = input(f"Enter new date (current: {meal.date}): ").strip()
                try:
                    datetime.strptime(meal.date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    return
                print(f"Updated meal: {meal}")
            else:
                print("Invalid meal number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_meal(self):
        self.view_meals()
        if not self.meals:
            return
        try:
            index = int(input("Enter the number of the meal to delete: ")) - 1
            if 0 <= index < len(self.meals):
                meal = self.meals.pop(index)
                print(f"Deleted meal: {meal.name}")
            else:
                print("Invalid meal number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_total_calories(self):
        total_calories = sum(meal.calories for meal in self.meals)
        print(f"Total daily calories: {total_calories}")

    def run(self):
        while True:
            print("\nCalorie Tracker")
            print("1. Add Meal")
            print("2. View Meals")
            print("3. Update Meal")
            print("4. Delete Meal")
            print("5. Calculate Total Calories")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_meal()
            elif choice == '2':
                self.view_meals()
            elif choice == '3':
                self.update_meal()
            elif choice == '4':
                self.delete_meal()
            elif choice == '5':
                self.calculate_total_calories()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    CalorieTracker()
