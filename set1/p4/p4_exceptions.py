# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P4 - Safe Menu Program
# Date: 11-21-2026


def divide_numbers():
    try:
        dividend = float(input("Enter the first number (dividend): "))
        divisor = float(input("Enter the second number (divisor): "))
        result = dividend / divisor
    except ValueError:
        print("Error: That is not a valid number. Please use digits only.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    else:
        print(f"Result: {dividend:g} / {divisor:g} = {result:g}")
    finally:
        print("Division attempt finished.")


def show_text_file():
    filename = input("Enter the file name (example: sample.txt): ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f'Error: The file "{filename}" was not found.')
    else:
        print(f"\n----- {filename} -----")
        print(contents)
        print("----- end of file -----")
    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("Prepared by: Samantha Ondoy (IV-BSIT-A)")
        print("1. Divide two numbers")
        print("2. Open and display a text file")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            show_text_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(f'Invalid choice "{choice}". Please enter 1, 2, or 3.')


if __name__ == "__main__":
    main()
