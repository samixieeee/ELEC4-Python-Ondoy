# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P3 - Student Record Manager
# Date: 11-21-2026

student_names = []
name_keys = set()


def clean_name(name):
    return " ".join(name.split())


def add_student(name):
    name = clean_name(name)
    if not name:
        print("Name cannot be empty.")
        return
    key = name.lower()
    if key in name_keys:
        print(f'"{name}" is already in the records. Duplicate not added.')
        return
    student_names.append(name)
    name_keys.add(key)
    print(f'"{name}" was added.')


def remove_student(name):
    key = clean_name(name).lower()
    if key not in name_keys:
        print(f'"{name}" was not found.')
        return
    for saved_name in student_names:
        if saved_name.lower() == key:
            student_names.remove(saved_name)
            name_keys.remove(key)
            print(f'"{saved_name}" was removed.')
            return


def search_students(keyword):
    keyword = clean_name(keyword).lower()
    matches = [name for name in student_names if keyword in name.lower()]
    if matches:
        print(f'Found {len(matches)} match(es) for "{keyword}":')
        for name in sorted(matches, key=str.lower):
            print(" -", name)
    else:
        print(f'No student matches "{keyword}".')


def display_students():
    if not student_names:
        print("No students recorded yet.")
        return
    print("\n----- STUDENT LIST (A-Z) -----")
    for number, name in enumerate(sorted(student_names, key=str.lower), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(student_names)}")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("Prepared by: Samantha Ondoy (IV-BSIT-A)")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(input("Enter full name: "))
        elif choice == "2":
            remove_student(input("Enter the full name to remove: "))
        elif choice == "3":
            search_students(input("Enter a name or part of a name: "))
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()

# LIST VS SET:
# A list keeps items in order, allows duplicates, and lets us loop, sort, and number
# the entries. A set has no order and keeps only unique items, which makes checking
# "is this already here?" very fast. This program stores the real names in the list
# student_names so they can be displayed alphabetically with their original capitalization.
# It stores lowercase copies in the set name_keys, so "Kevin Minion" and
# "kevin minion" are detected as the same student before anything is added.
