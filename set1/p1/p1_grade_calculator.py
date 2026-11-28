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


# function 6: display the grade report
# function 6: display the grade report
def display_results(grades):
    print("\n===== STUDENT GRADE REPORT =====")
    print("Student:", STUDENT_NAME)

    print("\nGrades:")
    for number, grade in enumerate(grades, start=1):
        print(f"{number}. {grade}")

    print("\nAverage:", round(calculate_average(grades), 2))
    print("Highest Grade:", get_highest_grade(grades))
    print("Lowest Grade:", get_lowest_grade(grades))
    print("Status:", check_status(grades))
    print("================================")


# function 7: main menu
def main():
    grades = []

    while True:
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            grades = get_grades()
            print("Grades saved successfully.")

        elif choice == "2":
            if len(grades) > 0:
                display_results(grades)
            else:
                print("\nPlease enter grades first.")

        elif choice == "3":
            print("Calculator exited.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# LOCAL AND GLOBAL VARIABLES:
# A local variable is created inside a function and can only be used there.
# For example, grades inside main() is a local variable.
# A global variable is declared outside functions and can be accessed by
# different functions. In this program, STUDENT_NAME and PASSING_GRADE
# are global variables used by the grade calculator.