
"""
Student: LEE HARVEY OSWALD MUNAR
Section: IV-BSIT-B
Activity: P3 - Student Record Manager
Date: 2026-11-26
"""

students = []
student_names = set()


# function 1: add a student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name.casefold() in student_names:
        print("Student already exists.")
    else:
        students.append(name)
        student_names.add(name.casefold())
        print("Student added successfully.")


# function 2: remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_names.remove(student.casefold())
            print("Student removed successfully.")
            return

    print("Student not found.")


# function 3: search for a student
def search_student():
    query = input("Enter all or part of a student name: ").strip().casefold()

    if not query:
        print("Search cannot be empty.")
        return

    found = False

    for student in students:
        if query in student.casefold():
            print(student)
            found = True

    if not found:
        print("No matching student found.")


# function 4: display all students
def display_students():
    if not students:
        print("No students in the records.")
        return

    print("\n===== STUDENT RECORDS =====")

    sorted_students = sorted(students, key=str.casefold)

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print("Total students:", len(students))
    print("===========================")


# function 5: main menu
def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Program exited.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# list and set explanation:
# A list stores multiple items and keeps their original order.
# I used a list to store student names.
# A set stores unique values and prevents duplicate entries.
# I used a set to check whether a student name already exists.