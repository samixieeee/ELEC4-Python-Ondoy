# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P2 - Custom Module (student_utils module)
# Date: 11-21-2026

PASSING_AVERAGE = 75


def get_average(grades):
    return sum(grades) / len(grades)


def get_remarks(grades):
    if get_average(grades) >= PASSING_AVERAGE:
        return "PASSED"
    return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)
