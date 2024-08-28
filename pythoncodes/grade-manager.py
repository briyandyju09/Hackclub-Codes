import json
import os

class GradesManager:
    def __init__(self, filename="grades.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)
        self.load()

    def load(self):
        with open(self.filename, "r") as f:
            self.grades = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.grades, f, indent=4)

    def add_grade(self, student_name, subject, grade):
        if student_name not in self.grades:
            self.grades[student_name] = {}
        self.grades[student_name][subject] = grade
        self.save()
        print(f"Added grade for {student_name} in {subject}: {grade}")

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = 0
        count = 0
        for subjects in self.grades.values():
            for grade in subjects.values():
                total_grades += grade
                count += 1
        return total_grades / count if count else 0

    def list_grades(self):
        if not self.grades:
            print("No grades recorded.")
            return
        for student_name, subjects in self.grades.items():
            print(f"Student: {student_name}")
            for subject, grade in subjects.items():
                print(f"  Subject: {subject}, Grade: {grade}")

def main():
    manager = GradesManager()
    
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Grade")
        print("2. View Average Grade")
        print("3. List All Grades")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            manager.add_grade(student_name, subject, grade)

        elif choice == "2":
            avg = manager.average_grade()
            print(f"Average Grade: {avg:.2f}")

        elif choice == "3":
            manager.list_grades()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
