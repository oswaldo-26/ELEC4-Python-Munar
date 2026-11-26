
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