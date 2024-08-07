class Workout:
    def __init__(self, date, activity, duration):
        self.date = date
        self.activity = activity
        self.duration = duration

    def __str__(self):
        return f"Date: {self.date}, Activity: {self.activity}, Duration: {self.duration} minutes"

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.run()

    def add_workout(self):
        date = input("Enter workout date (YYYY-MM-DD): ").strip()
        activity = input("Enter workout activity: ").strip()
        try:
            duration = int(input("Enter workout duration (in minutes): ").strip())
        except ValueError:
            print("Invalid duration. Please enter a number.")
            return
        workout = Workout(date, activity, duration)
        self.workouts.append(workout)
        print(f"Added workout: {workout}")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts available.")
        else:
            for i, workout in enumerate(self.workouts):
                print(f"{i+1}. {workout}")

    def update_workout(self):
        self.view_workouts()
        if not self.workouts:
            return
        try:
            index = int(input("Enter the number of the workout to update: ")) - 1
            if 0 <= index < len(self.workouts):
                workout = self.workouts[index]
                workout.date = input(f"Enter new date (current: {workout.date}): ").strip()
                workout.activity = input(f"Enter new activity (current: {workout.activity}): ").strip()
                try:
                    workout.duration = int(input(f"Enter new duration (current: {workout.duration}): ").strip())
                except ValueError:
                    print("Invalid duration. Please enter a number.")
                    return
                print(f"Updated workout: {workout}")
            else:
                print("Invalid workout number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_workout(self):
        self.view_workouts()
        if not self.workouts:
            return
        try:
            index = int(input("Enter the number of the workout to delete: ")) - 1
            if 0 <= index < len(self.workouts):
                workout = self.workouts.pop(index)
                print(f"Deleted workout: {workout}")
            else:
                print("Invalid workout number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_total_duration(self):
        total_duration = sum(workout.duration for workout in self.workouts)
        print(f"Total workout duration: {total_duration} minutes")

    def run(self):
        while True:
            print("\nFitness Tracker")
            print("1. Add Workout")
            print("2. View Workouts")
            print("3. Update Workout")
            print("4. Delete Workout")
            print("5. Calculate Total Duration")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_workout()
            elif choice == '2':
                self.view_workouts()
            elif choice == '3':
                self.update_workout()
            elif choice == '4':
                self.delete_workout()
            elif choice == '5':
                self.calculate_total_duration()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    FitnessTracker()
