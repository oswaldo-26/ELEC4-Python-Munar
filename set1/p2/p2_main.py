
"""
Student: LEE HARVEY OSWALD MUNAR
Section: IV-BSIT-B
Activity: P2 - Custom Module: student_utils
Date: 2026-11-25
"""

import student_utils
from student_utils import calculate_average, get_highest_grade
from datetime import datetime


STUDENT_NAME = "LEE HARVEY OSWALD MUNAR"


# function 1: accept and validate grades
def get_grades():
    grades = []

    while True:
        entry = input("Enter a grade (or type done): ")

        if entry.lower() == "done":
            if grades:
                return grades
            print("Please enter at least one grade.")

        else:
            try:
                grade = float(entry)

                if 0 <= grade <= 100:
                    grades.append(grade)
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")