"""
report.py
---------
Functional Module 3: Reports
- Show a full summary of all students and their GPA
- Save the report to a text file
"""

import os
from datetime import datetime
from storage import load_students
from grades import calculate_gpa, get_letter_grade


REPORTS_FOLDER = "reports"


def show_report():
    """Print a full class report to the screen."""
    students = load_students()

    if not students:
        print("\n[!] No students found. Add some first.")
        return

    print("\n" + "=" * 45)
    print("        STUDENT PERFORMANCE REPORT")
    print("=" * 45)

    for s in students:
        print(f"\n  ID   : {s['id']}")
        print(f"  Name : {s['name']}")

        if s["grades"]:
            gpa = calculate_gpa(s["grades"])
            grade = get_letter_grade(gpa)
            print(f"  GPA  : {gpa}/10  [{grade}]")
        else:
            print(f"  GPA  : No grades recorded")

        print("  " + "-" * 30)

    print(f"\n  Total Students: {len(students)}")
    print("=" * 45)


def save_report():
    """Save the full class report to a .txt file in the reports folder."""
    students = load_students()

    if not students:
        print("\n[!] No students found. Nothing to save.")
        return

    # Create reports folder if it does not exist
    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    # Create a filename with the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORTS_FOLDER, f"report_{timestamp}.txt")

    lines = []
    lines.append("=" * 45)
    lines.append("      STUDENT PERFORMANCE REPORT")
    lines.append(f"  Date: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
    lines.append("=" * 45)

    for s in students:
        lines.append(f"\n  ID   : {s['id']}")
        lines.append(f"  Name : {s['name']}")
        if s["grades"]:
            gpa = calculate_gpa(s["grades"])
            lines.append(f"  GPA  : {gpa}/10  [{get_letter_grade(gpa)}]")
            for subject, marks in s["grades"].items():
                lines.append(f"    {subject}: {marks}/100")
        else:
            lines.append("  GPA  : No grades recorded")
        lines.append("  " + "-" * 30)

    lines.append(f"\n  Total Students: {len(students)}")
    lines.append("=" * 45)

    with open(filename, "w") as f:
        f.write("\n".join(lines))

    print(f"[✓] Report saved to: {filename}")


def menu():
    """Report sub-menu."""
    while True:
        print("\n--- Reports ---")
        print("  1. Show Report on Screen")
        print("  2. Save Report to File")
        print("  3. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            show_report()
        elif choice == "2":
            save_report()
        elif choice == "3":
            break
        else:
            print("[!] Enter 1, 2, or 3.")
