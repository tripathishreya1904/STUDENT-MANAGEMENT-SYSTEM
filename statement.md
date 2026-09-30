# Project Statement

## Problem Statement

Managing student records manually on paper or in spreadsheets is slow and error-prone.
This project provides a simple command-line tool to store student information,
track their grades, and view performance reports — all from a terminal.

---

## Scope of the Project

**Included:**
- Adding and removing students (name and ID)
- Searching students by name or ID
- Adding subject marks and calculating GPA automatically
- Generating a class performance report saved as a text file
- Storing all data in a plain Python file (no database or internet needed)

**Not Included:**
- Graphical user interface (GUI)
- Login or password system
- Online or cloud storage

---

## Target Users

- Teachers or tutors managing a small group of students
- Students learning Python who want to see a real working project

---

## High-Level Features

1. **Student Management** — Add students (name + auto ID), remove by ID, search by name or ID
2. **Grade & GPA** — Add marks per subject, GPA is calculated automatically from marks
3. **Reports** — View a full performance summary on screen or save it as a `.txt` file

---

## Non-Functional Requirements

1. **Usability** — Simple numbered menus that anyone can follow without instructions
2. **Reliability** — Data is saved to a file after every change so nothing is lost
3. **Performance** — All operations complete instantly for a typical class size
4. **Error Handling** — All inputs are checked before being accepted; invalid input shows a clear message
5. **Maintainability** — Each feature lives in its own file making the code easy to read and update
6. **Portability** — Works on Windows, Mac, and Linux with only Python installed

---

## Course Relevance — Python Essentials Concepts Used

| Concept              | Where Used                                      |
|---------------------|-------------------------------------------------|
| Variables & types    | Storing student name, ID, marks                 |
| Lists & dictionaries | Student records stored as list of dictionaries  |
| Functions            | Each action is its own function                 |
| File I/O             | Reading and writing `students_data.py`          |
| if / elif / else     | Input validation and menu choices               |
| for loops            | Searching and displaying student records        |
| Arithmetic           | Calculating average marks and GPA               |
| Modular code         | Separate `.py` files for each feature           |
