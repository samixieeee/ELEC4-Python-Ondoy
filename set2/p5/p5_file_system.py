# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P5 - Student Information File System
# Date: 11-21-2026

import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")
SEPARATOR = "|"


def load_students():
    students = []
    if not os.path.exists(DATA_FILE):
        print("students.txt not found. Starting with an empty list.")
        return students
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(SEPARATOR)
            if len(parts) != 4:
                continue
            try:
                average = float(parts[3])
            except ValueError:
                continue
            students.append({"id": parts[0], "name": parts[1],
                             "course": parts[2], "average": average})
    print(f"Loaded {len(students)} record(s) from students.txt.")
    return students


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for s in students:
            file.write(f"{s['id']}{SEPARATOR}{s['name']}{SEPARATOR}"
                       f"{s['course']}{SEPARATOR}{s['average']:.2f}\n")


def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text and SEPARATOR not in text:
            return text
        print(f"Please type something (the '{SEPARATOR}' character is not allowed).")


def ask_average(prompt):
    while True:
        try:
            average = float(input(prompt))
        except ValueError:
            print("Invalid average. Please enter a number such as 88.5.")
            continue
        if 0 <= average <= 100:
            return average
        print("Average must be from 0 to 100.")


def find_student(students, student_id):
    for s in students:
        if s["id"].lower() == student_id.lower():
            return s
    return None


def print_student(s):
    print(f"{s['id']:<12}{s['name']:<25}{s['course']:<16}{s['average']:>7.2f}")


def print_header():
    print(f"{'ID':<12}{'Full Name':<25}{'Course/Sec':<16}{'Average':>7}")
    print("-" * 60)


def add_student(students):
    student_id = ask_text("Student ID: ")
    if find_student(students, student_id):
        print("That ID already exists.")
        return
    students.append({"id": student_id,
                     "name": ask_text("Full name: "),
                     "course": ask_text("Course/Section: "),
                     "average": ask_average("General average: ")})
    save_students(students)
    print("Student added and saved.")


def display_students(students):
    if not students:
        print("No records yet.")
        return
    print_header()
    for s in students:
        print_student(s)
    print(f"Total records: {len(students)}")


def search_student(students):
    s = find_student(students, ask_text("Enter Student ID to search: "))
    if s:
        print_header()
        print_student(s)
    else:
        print("No student has that ID.")


def update_student(students):
    s = find_student(students, ask_text("Enter Student ID to update: "))
    if not s:
        print("No student has that ID.")
        return
    print("Current record:")
    print_header()
    print_student(s)
    print("Press Enter to keep the current value.")

    new_name = input(f"Full name [{s['name']}]: ").strip()
    new_course = input(f"Course/Section [{s['course']}]: ").strip()
    if new_name and SEPARATOR not in new_name:
        s["name"] = new_name
    if new_course and SEPARATOR not in new_course:
        s["course"] = new_course

    while True:
        new_average = input(f"General average [{s['average']:.2f}]: ").strip()
        if new_average == "":
            break
        try:
            value = float(new_average)
            if 0 <= value <= 100:
                s["average"] = value
                break
            print("Average must be from 0 to 100.")
        except ValueError:
            print("Invalid average. Please enter a number.")

    save_students(students)
    print("Record updated and saved.")


def main():
    students = load_students()
    while True:
        print("\n===== STUDENT INFORMATION FILE SYSTEM =====")
        print("Prepared by: Samantha Ondoy (IV-BSIT-A)")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search by ID")
        print("4. Update student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Goodbye! Your records are saved in students.txt.")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()
