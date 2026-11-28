
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


# function 3: main menu
def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Divide two numbers")
        print("2. Open a file")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Program exited.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



# the try block contains code that may cause an error.
# the except block handles errors and prevents the program from crashing.
# the else block runs only when no exception occurs in the try block.
# the finally block always runs, whether an error occurs or not.
# this program uses valueerror, zerodivisionerror, and filenotfounderror
# to handle invalid numbers, division by zero, and missing files.