"""
main.py
-------
Run this file to start the Student Management System.

    python main.py

All data is saved automatically to students_data.py
"""

import students
import grades
import report


def show_menu():
    print("\n" + "=" * 40)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Student Management")
    print("  2. Grades & GPA")
    print("  3. Reports")
    print("  4. Exit")
    print("=" * 40)


def main():
    print("\nWelcome to the Student Management System!")
    print("Data is saved automatically.\n")

    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            students.menu()
        elif choice == "2":
            grades.menu()
        elif choice == "3":
            report.menu()
        elif choice == "4":
            print("\nGoodbye! Your data is saved.\n")
            break
        else:
            print("[!] Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
