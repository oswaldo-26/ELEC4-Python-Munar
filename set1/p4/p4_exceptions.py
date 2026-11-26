
"""
Student: LEE HARVEY OSWALD MUNAR
Section: IV-BSIT-B
Activity: P4 - Safe Menu Program
Date: 2026-11-26
"""


# function 1: divide two numbers
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


# function 2: open and read a file
def open_file():
    filename = input("Enter the file name: ")

    try:
        with open(filename, "r") as file:
            contents = file.read()

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("You do not have permission to open this file.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(contents)
        print("=========================")

    finally:
        print("File operation finished.")