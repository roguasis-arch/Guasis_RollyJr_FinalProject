# src/student.py

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
