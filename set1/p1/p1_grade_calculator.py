# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: 11-21-2026

PASSING_AVERAGE = 75


def collect_grades():
    while True:
        count_text = input("How many grades will you enter? ")
        if count_text.isdigit() and int(count_text) > 0:
            count = int(count_text)
            break
        print("Please enter a whole number greater than 0.")

    grades = []
    for number in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade #{number} (0-100): "))
            except ValueError:
                print("Invalid input. Please type a number.")
                continue
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            print("Grade must be from 0 to 100.")
    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def find_highest(grades):
    return max(grades)


def find_lowest(grades):
    return min(grades)


def determine_remarks(grades):
    if calculate_average(grades) >= PASSING_AVERAGE:
        return "PASSED"
    return "FAILED"


def show_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("Prepared by: Samantha Ondoy (IV-BSIT-A)")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            grades = collect_grades()
            print(f"{len(grades)} grade(s) saved.")
        elif choice == "2":
            if not grades:
                print("No grades yet. Please choose option 1 first.")
                continue
            print("\n----- RESULTS -----")
            print("Grades entered :", ", ".join(f"{g:g}" for g in grades))
            print(f"Average        : {calculate_average(grades):.2f}")
            print(f"Highest grade  : {find_highest(grades):g}")
            print(f"Lowest grade   : {find_lowest(grades):g}")
            print(f"Remarks        : {determine_remarks(grades)}")
        elif choice == "3":
            print("Goodbye, Samantha!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

# SCOPE EXPLANATION:
# A local variable exists only inside the function where it is created, like the
# "grades" list inside collect_grades() and the "grades" list inside main().
# Because main() cannot see the list built inside collect_grades(), that function
# returns it and main() stores the returned value in its own local variable.
# PASSING_AVERAGE is a global variable defined at the top of the file, so any
# function, such as determine_remarks(), can read it without receiving it as a parameter.
