# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P2 - Custom Module (main program)
# Date: 11-21-2026

import datetime
import student_utils
from student_utils import get_highest, get_lowest


def read_grades():
    grades = []
    while True:
        count_text = input("How many grades will you enter? ")
        if count_text.isdigit() and int(count_text) > 0:
            break
        print("Please enter a whole number greater than 0.")

    for number in range(1, int(count_text) + 1):
        while True:
            try:
                grade = float(input(f"Enter grade #{number} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Invalid input. Please type a number.")
    return grades


def main():
    print("===== STUDENT GRADE REPORT =====")
    student_name = input("Student name: ").strip() or "Samantha Ondoy"
    grades = read_grades()

    average = student_utils.get_average(grades)
    remarks = student_utils.get_remarks(grades)
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    generated_at = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

    print("\n----- REPORT -----")
    print(f"Student   : {student_name}")
    print(f"Grades    : {', '.join(f'{g:g}' for g in grades)}")
    print(f"Average   : {average:.2f}")
    print(f"Highest   : {highest:g}")
    print(f"Lowest    : {lowest:g}")
    print(f"Remarks   : {remarks}")
    print(f"Generated : {generated_at}")
    print("Prepared by: Samantha Ondoy (IV-BSIT-A)")


if __name__ == "__main__":
    main()
