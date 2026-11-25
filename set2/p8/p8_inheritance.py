# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P8 - Inheritance and Polymorphism
# Date: 11-21-2026


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, I am {self.name}, {self.age} years old."


class Student(Person):
    def __init__(self, name, age, course, year_level):
        super().__init__(name, age)
        self.course = course
        self.year_level = year_level

    def introduce(self):
        return (f"Hi! I'm {self.name}, a {self.year_level} {self.course} student, "
                f"{self.age} years old.")


class Teacher(Person):
    def __init__(self, name, age, subject, years_teaching):
        super().__init__(name, age)
        self.subject = subject
        self.years_teaching = years_teaching

    def introduce(self):
        return (f"Good day. I am {self.name}, and I have taught {self.subject} "
                f"for {self.years_teaching} years.")


def main():
    print("===== INHERITANCE AND POLYMORPHISM =====")
    print("Prepared by: Samantha Ondoy (IV-BSIT-A)\n")

    people = [
        Person("Dr. Nefario", 70),
        Student("Samantha Ondoy", 21, "BSIT", "4th-year"),
        Teacher("Mr. Gru", 38, "Python Programming", 12),
        Student("Phil Minion", 20, "BSCS", "3rd-year"),
    ]

    for person in people:
        print(f"[{type(person).__name__}] {person.introduce()}")


if __name__ == "__main__":
    main()

# HOW THIS DEMONSTRATES INHERITANCE AND POLYMORPHISM:
# Student and Teacher inherit from Person, so they automatically get the name and age
# attributes by calling super().__init__() instead of rewriting that code.
# Each child class adds its own attributes (course and year_level, or subject and
# years_teaching) and overrides introduce() to produce its own message.
# Polymorphism appears in the for loop: every object is treated the same way with
# person.introduce(), yet Python runs the version that matches each object's class.
