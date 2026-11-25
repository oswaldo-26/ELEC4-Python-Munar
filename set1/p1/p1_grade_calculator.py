"""
Student: LEE HARVEY OSWALD MUNAR
Section: IV-BSIT-B
Activity: P1 - Student Grade Calculator
Date: 2026-11-25
"""

STUDENT_NAME = "LEE HARVEY OSWALD MUNAR"
PASSING_GRADE = 75


# function 1: accept and validate student grades
def get_grades():
    grades = []

    while True:
        entry = input("Enter a grade (or type done): ")

        if entry.lower() == "done":
            if len(grades) > 0:
                return grades
            else:
                print("Please enter at least one grade.")

        else:
            try:
                grade = float(entry)

                if grade >= 0 and grade <= 100:
                    grades.append(grade)
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")


# function 2: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# function 3: Get the highest grade
def get_highest_grade(grades):
    return max(grades)


# function 4: Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)


# function 5: Check pass or fail
def check_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"
