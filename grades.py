"""
grades.py
---------
Functional Module 2: Grade & GPA Management
- Add marks for a subject
- Calculate GPA from marks
- View grades for a student
"""

from storage import load_students, save_students


def get_letter_grade(gpa):
    """
    Convert a GPA (out of 10) to a letter grade.
    Simple if-elif chain — easy to read.
    """
    if gpa >= 9.0:
        return "O  (Outstanding)"
    elif gpa >= 8.0:
        return "A+ (Excellent)"
    elif gpa >= 7.0:
        return "A  (Very Good)"
    elif gpa >= 6.0:
        return "B+ (Good)"
    elif gpa >= 5.0:
        return "B  (Average)"
    elif gpa >= 4.0:
        return "C  (Pass)"
    else:
        return "F  (Fail)"


def calculate_gpa(grades):
    """
    Given a dictionary of {subject: marks}, calculate GPA out of 10.
    GPA = (average marks) / 10
    """
    if not grades:
        return 0.0
    total = sum(grades.values())       # add up all marks
    average = total / len(grades)      # divide by number of subjects
    gpa = round(average / 10, 2)       # convert to GPA out of 10
    return gpa


def add_grade():
    """Add a subject and marks for a student."""
    print("\n--- Add Grade ---")

    sid = input("Enter Student ID: ").strip()
    if not sid.isdigit():
        print("[!] ID must be a number.")
        return

    students = load_students()
    found = False

    for s in students:
        if s["id"] == int(sid):
            found = True
            print(f"Adding grade for: {s['name']}")

            subject = input("Enter subject name: ").strip()
            if not subject:
                print("[!] Subject cannot be empty.")
                return

            marks = input(f"Enter marks for {subject} (0-100): ").strip()
            if not marks.isdigit() or not (0 <= int(marks) <= 100):
                print("[!] Marks must be a number from 0 to 100.")
                return

            # Save the grade into this student's grades dictionary
            s["grades"][subject] = int(marks)
            save_students(students)
            print(f"[✓] Saved: {subject} = {marks}/100 for {s['name']}")
            break

    if not found:
        print(f"[!] No student found with ID {sid}.")


def view_grades():
    """Show all grades and the calculated GPA for a student."""
    print("\n--- View Grades & GPA ---")

    sid = input("Enter Student ID: ").strip()
    if not sid.isdigit():
        print("[!] ID must be a number.")
        return

    students = load_students()
    for s in students:
        if s["id"] == int(sid):
            print(f"\n  Student : {s['name']}  (ID: {s['id']})")

            if not s["grades"]:
                print("  No grades added yet.")
                return

            print(f"\n  {'Subject':<20} {'Marks':>6}")
            print("  " + "-" * 28)
            for subject, marks in s["grades"].items():
                print(f"  {subject:<20} {marks:>5}/100")

            gpa = calculate_gpa(s["grades"])
            print("  " + "-" * 28)
            print(f"\n  GPA   : {gpa} / 10")
            print(f"  Grade : {get_letter_grade(gpa)}")
            return

    print(f"[!] No student found with ID {sid}.")


def menu():
    """Grade Management sub-menu."""
    while True:
        print("\n--- Grade & GPA Management ---")
        print("  1. Add Grade for a Student")
        print("  2. View Grades & GPA")
        print("  3. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            break
        else:
            print("[!] Enter 1, 2, or 3.")
