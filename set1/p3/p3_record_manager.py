
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