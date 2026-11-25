# Name: Samantha Ondoy
# Section: IV-BSIT-A
# Activity: P7 - Student Management System with Classes
# Date: 11-21-2026


class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def __str__(self):
        return f"{self.code} - {self.title}"


class Student:
    def __init__(self, student_id, name, subject, grade):
        self.student_id = student_id
        self.name = name
        self.subject = subject
        self.__grade = 0
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if isinstance(new_grade, (int, float)) and 0 <= new_grade <= 100:
            self.__grade = new_grade
            return True
        print(f"  Rejected: {new_grade!r} is not a valid grade for {self.name} (0-100 only).")
        return False

    def update_info(self, name=None, subject=None):
        if name:
            self.name = name
        if subject:
            self.subject = subject

    def display(self):
        print(f"  [{self.student_id}] {self.name:<18} | {self.subject} | Grade: {self.__grade}")


class Section:
    def __init__(self, name, adviser):
        self.name = name
        self.adviser = adviser
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def list_students(self):
        print(f"\nSection {self.name} (Adviser: {self.adviser}) - {len(self.students)} student(s)")
        for student in self.students:
            student.display()


def main():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("Prepared by: Samantha Ondoy (IV-BSIT-A)")

    python_subject = Subject("ELEC 4", "Python Programming")
    node_subject = Subject("ELEC 3", "Node.js")

    section = Section("IV-BSIT-A", "Prof. Gru")
    section.add_student(Student("S-001", "Samantha Ondoy", python_subject, 92))
    section.add_student(Student("S-002", "Otto Minion", python_subject, 85))
    section.add_student(Student("S-003", "Carl Minion", node_subject, 79))

    print("\nBEFORE UPDATE:")
    section.list_students()

    print("\nUPDATING S-002 ...")
    otto = section.find_student("S-002")
    otto.set_grade(150)
    otto.set_grade("ninety")
    otto.set_grade(89)
    otto.update_info(name="Otto B. Minion", subject=node_subject)
    print(f"  S-002 grade read through get_grade(): {otto.get_grade()}")

    print("\nAFTER UPDATE:")
    section.list_students()


if __name__ == "__main__":
    main()
