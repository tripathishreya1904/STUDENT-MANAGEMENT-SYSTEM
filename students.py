"""
students.py
-----------
Functional Module 1: Student Management
- Add a student (name + ID only)
- Remove a student by ID
- Search a student by name or ID
"""

from storage import load_students, save_students, append_student, get_next_id


def add_student():
    """Ask for a name and assign an ID, then append to storage."""
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    if not name:
        print("[!] Name cannot be empty.")
        return

    # Auto-generate ID
    new_id = get_next_id()

    new_student = {
        "id": new_id,
        "name": name,
        "grades": {}   # grades will be added later via grades.py
    }

    append_student(new_student)
    print(f"[✓] Student '{name}' added. Their ID is: {new_id}")


def remove_student():
    """Remove a student from storage using their ID."""
    print("\n--- Remove Student ---")

    sid = input("Enter Student ID to remove: ").strip()
    if not sid.isdigit():
        print("[!] ID must be a number.")
        return

    students = load_students()

    # Find the student first
    target = None
    for s in students:
        if s["id"] == int(sid):
            target = s
            break

    if not target:
        print(f"[!] No student found with ID {sid}.")
        return

    confirm = input(f"Remove '{target['name']}' (ID: {sid})? (yes/no): ").strip().lower()
    if confirm == "yes":
        # Keep everyone except the one being removed
        updated = [s for s in students if s["id"] != int(sid)]
        save_students(updated)
        print(f"[✓] '{target['name']}' has been removed.")
    else:
        print("Cancelled.")


def search_by_name():
    """Search students by typing part of their name."""
    print("\n--- Search by Name ---")

    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("[!] Please enter something.")
        return

    students = load_students()
    # Match any student whose name contains the typed text
    results = [s for s in students if query in s["name"].lower()]

    if not results:
        print(f"[!] No student found with name containing '{query}'.")
        return

    print(f"\nFound {len(results)} result(s):\n")
    print(f"  {'ID':<8} {'Name'}")
    print("  " + "-" * 25)
    for s in results:
        print(f"  {s['id']:<8} {s['name']}")


def search_by_id():
    """Search and show a student by their exact ID."""
    print("\n--- Search by ID ---")

    sid = input("Enter Student ID: ").strip()
    if not sid.isdigit():
        print("[!] ID must be a number.")
        return

    students = load_students()
    for s in students:
        if s["id"] == int(sid):
            print(f"\n  ID   : {s['id']}")
            print(f"  Name : {s['name']}")
            if s["grades"]:
                print(f"  Subjects: {', '.join(s['grades'].keys())}")
            else:
                print(f"  Grades: None added yet")
            return

    print(f"[!] No student found with ID {sid}.")


def view_all():
    """Show all students in a simple list."""
    students = load_students()

    if not students:
        print("\n[!] No students yet. Add some first.")
        return

    print(f"\n  {'ID':<8} {'Name'}")
    print("  " + "-" * 25)
    for s in students:
        print(f"  {s['id']:<8} {s['name']}")
    print(f"\n  Total: {len(students)} student(s)")


def menu():
    """Student Management sub-menu."""
    while True:
        print("\n--- Student Management ---")
        print("  1. Add Student")
        print("  2. Remove Student")
        print("  3. Search by Name")
        print("  4. Search by ID")
        print("  5. View All Students")
        print("  6. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            search_by_id()
        elif choice == "5":
            view_all()
        elif choice == "6":
            break
        else:
            print("[!] Enter a number between 1 and 6.")
