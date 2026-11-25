# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P6 - Recursion Toolkit
# Date: 11-21-2026

import sys

sys.setrecursionlimit(3000)
MAX_N = 500


# Base case: n is 0 or 1 -> return 1
# Recursive call: n * factorial(n - 1)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Indexing convention (0-based): fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1 ...
# Base case: n is 0 or 1 -> return n
# Recursive call: fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Base case: n is 0 -> return 0
# Recursive call: n + sum_numbers(n - 1)
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case 1: empty list -> return False
# Base case 2: first item equals target -> return True
# Recursive call: search(items[1:], target)  (search the rest of the list)
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def ask_whole_number(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and minimum <= int(text) <= maximum:
            return int(text)
        print(f"Please enter a whole number from {minimum} to {maximum}.")


def main():
    while True:
        print("\n===== RECURSION TOOLKIT =====")
        print("Prepared by: Samantha Ondoy (IV-BSIT-A)")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of numbers 1 to n")
        print("4. Search a list")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            n = ask_whole_number("Enter n (0-500): ", 0, MAX_N)
            print(f"{n}! = {factorial(n)}")
        elif choice == "2":
            n = ask_whole_number("Enter n (1-100): ", 1, 100)
            terms = [fibonacci(i) for i in range(n)]
            print(f"First {n} terms (F(0) to F({n - 1})): {', '.join(map(str, terms))}")
            print(f"fibonacci({n}) = F({n}) = {fibonacci(n)}  (0-based: F(0)=0, F(1)=1)")
        elif choice == "3":
            n = ask_whole_number("Enter n (1-500): ", 1, MAX_N)
            print(f"Sum of 1 to {n} = {sum_numbers(n)}")
        elif choice == "4":
            raw = input("Enter items separated by commas (e.g. apple, mango, 5): ")
            items = [item.strip() for item in raw.split(",") if item.strip()]
            if not items:
                print("The list cannot be empty.")
                continue
            if len(items) > MAX_N:
                print(f"Please enter at most {MAX_N} items.")
                continue
            target = input("Enter the item to search for: ").strip()
            if not target:
                print("The search item cannot be empty.")
                continue
            found = search(items, target)
            print(f"List: {items}")
            print(f'search(items, "{target}") -> {found}')
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()
