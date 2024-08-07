class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}"

class GradeManager:
    def __init__(self):
        self.students = []
        self.run()

    def add_student(self):
        name = input("Enter student's name: ").strip()
        try:
            grade = float(input("Enter student's grade: ").strip())
        except ValueError:
            print("Invalid grade. Please enter a number.")
            return
        student = Student(name, grade)
        self.students.append(student)
        print(f"Added student: {student}")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            for i, student in enumerate(self.students):
                print(f"{i+1}. {student}")

    def update_student(self):
        self.view_students()
        if not self.students:
            return
        try:
            index = int(input("Enter the number of the student to update: ")) - 1
            if 0 <= index < len(self.students):
                student = self.students[index]
                student.name = input(f"Enter new name (current: {student.name}): ").strip()
                try:
                    student.grade = float(input(f"Enter new grade (current: {student.grade}): ").strip())
                except ValueError:
                    print("Invalid grade. Please enter a number.")
                    return
                print(f"Updated student: {student}")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_student(self):
        self.view_students()
        if not self.students:
            return
        try:
            index = int(input("Enter the number of the student to delete: ")) - 1
            if 0 <= index < len(self.students):
                student = self.students.pop(index)
                print(f"Deleted student: {student}")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_average_grade(self):
        if not self.students:
            print("No students available to calculate average.")
        else:
            total_grade = sum(student.grade for student in self.students)
            average_grade = total_grade / len(self.students)
            print(f"Average grade: {average_grade:.2f}")

    def run(self):
        while True:
            print("\nGrade Manager")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Calculate Average Grade")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.calculate_average_grade()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    GradeManager()