
"""
Student: LEE HARVEY OSWALD MUNAR
Section: IV-BSIT-B
Activity: P2 - Custom Module: student_utils
Date: 2026-11-25
"""

PASSING_GRADE = 75


# function 1: calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# function 2: determine pass or fail
def get_pass_fail_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


# function 3: get the highest grade
def get_highest_grade(grades):
    return max(grades)


# function  4: get the lowest grade
def get_lowest_grade(grades):
    return min(grades)