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
