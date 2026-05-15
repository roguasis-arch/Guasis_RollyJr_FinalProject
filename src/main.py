"""
Student Module

Contains the Student class used for storing student data.
"""


class Student:
    """Represents a student."""

    def __init__(self, name, grade):
        """
        Initialize student object.

        Args:
            name (str): Student name
            grade (float): Student grade
        """
        self.name = name
        self.grade = grade

    def get_status(self):
        """
        Determine if student passed or failed.
        """
        return "Passed" if self.grade >= 75 else "Failed"

    def to_dict(self):
        """
        Convert object into dictionary.
        """
        return {
            "name": self.name,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Student object from dictionary.
        """
        return cls(data["name"], data["grade"])

    def __str__(self):
        """
        String representation of student.
        """
        return (
            f"Name: {self.name} | "
            f"Grade: {self.grade} | "
            f"Status: {self.get_status()}"
        )


---

# src/manager.py

"""
Manager Module

Handles student management and file handling.
"""

import json
from student import Student


class GradeManager:
    """Handles student grade management."""

    def __init__(self, filename="storage.json"):
        """
        Initialize grade manager.

        Args:
            filename (str): JSON filename
        """
        self.filename = filename
        self.students = []
        self.load_students()

    def add_student(self, student):
        """
        Add student record.
        """
        self.students.append(student)
        self.save_students()

    def view_students(self):
        """
        Display all student records.
        """
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n=== STUDENT RECORDS ===")

        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student}")

    def delete_student(self, index):
        """
        Delete student record.
        """
        if 0 <= index < len(self.students):
            deleted = self.students.pop(index)
            self.save_students()

            print(f"\nDeleted: {deleted}")

        else:
            print("\nInvalid student number.")

    def calculate_average(self):
        """
        Calculate average grade.
        """
        if not self.students:
            print("\nNo records available.")
            return

        average = sum(
            student.grade for student in self.students
        ) / len(self.students)

        print(f"\nAverage Grade: {average:.2f}")

    def highest_grade(self):
        """
        Display highest grade student.
        """
        if not self.students:
            print("\nNo records available.")
            return

        top_student = max(
            self.students,
            key=lambda student: student.grade
        )

        print("\n=== TOP STUDENT ===")
        print(top_student)

    def passed_students(self):
        """
        Display passed students.
        """
        passed = [
            student
            for student in self.students
            if student.grade >= 75
        ]

        if not passed:
            print("\nNo passed students.")
            return

        print("\n=== PASSED STUDENTS ===")

        for student in passed:
            print(student)

    def failed_students(self):
        """
        Display failed students.
        """
        failed = [
            student
            for student in self.students
            if student.grade < 75
        ]

        if not failed:
            print("\nNo failed students.")
            return

        print("\n=== FAILED STUDENTS ===")

        for student in failed:
            print(student)

    def search_student(self, keyword):
        """
        Search student by name.
        """
        found = [
            student
            for student in self.students
            if keyword.lower() in student.name.lower()
        ]

        if not found:
            print("\nStudent not found.")
            return

        print("\n=== SEARCH RESULT ===")

        for student in found:
            print(student)

    def save_students(self):
        """
        Save student records to JSON file.
        """
        data = [
            student.to_dict()
            for student in self.students
        ]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        """
        Load student records from JSON file.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                self.students = [
                    Student.from_dict(item)
                    for item in data
                ]

        except FileNotFoundError:
            self.students = []


---

# src/main.py

"""
Main Module

Runs the Student Grade Manager application.
"""

from manager import GradeManager
from student import Student


def display_menu():
    """
    Display application menu.
    """
    print("\n=== STUDENT GRADE MANAGER ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Calculate Average")
    print("5. Show Highest Grade")
    print("6. Show Passed Students")
    print("7. Show Failed Students")
    print("8. Search Student")
    print("9. Exit")


def main():
    """
    Main program function.
    """
    manager = GradeManager()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")

            try:
                grade = float(
                    input("Enter student grade: ")
                )

                if grade < 0 or grade > 100:
                    print(
                        "\nGrade must be between 0 and 100."
                    )
                    continue

                student = Student(name, grade)

                manager.add_student(student)

                print("\nStudent added successfully.")

            except ValueError:
                print("\nInvalid grade input.")

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.view_students()

            try:
                number = int(
                    input(
                        "\nEnter student number to delete: "
                    )
                )

                manager.delete_student(number - 1)

            except ValueError:
                print("\nInvalid input.")

        elif choice == "4":
            manager.calculate_average()

        elif choice == "5":
            manager.highest_grade()

        elif choice == "6":
            manager.passed_students()

        elif choice == "7":
            manager.failed_students()

        elif choice == "8":
            keyword = input(
                "Enter student name to search: "
            )

            manager.search_student(keyword)

        elif choice == "9":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
