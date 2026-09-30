# Student Management System

A command-line Python project for the **Python Essentials** course on VITyarthi.

---

## Overview

This system lets you manage student records from your terminal.
All data is stored in a plain Python file called `students_data.py` — no database needed.
Every time you add a student, their record gets **appended and saved automatically**.

---

## Features

- Add and remove students (name + ID only)
- Search students by name or by ID
- Add subject marks and automatically calculate GPA
- Generate and save a performance report as a `.txt` file

---

## Technologies Used

- Python 3.14
- No extra libraries needed — only built-in Python modules

---

## Project Structure

```
student_management_system/
│
├── main.py            ← Run this to start the app
├── students.py        ← Add, remove, search students
├── grades.py          ← Add marks, calculate GPA
├── report.py          ← Generate reports
├── storage.py         ← Save and load data from students_data.py
│
├── students_data.py   ← Created automatically; stores all data
├── reports/           ← Created automatically; saved report files
│
├── README.md
└── statement.md
```

---

## How to Run

### Step 1 — Check Python is installed
```
python --version
```
You need Python 3.13 or above.

### Step 2 — Clone or download this repository
```
git clone https://github.com/tripathishreya1904/STUDENT-MANAGEMENT-SYSTEM
cd student-management-system
```

### Step 3 — Run the app
```
python main.py
```

No `pip install` needed.

---

## How to Use

You will see this menu:

```
========================================
    STUDENT MANAGEMENT SYSTEM
========================================
  1. Student Management
  2. Grades & GPA
  3. Reports
  4. Exit
========================================
```

**Recommended order for first use:**
1. Press `1` → Add a student
2. Press `2` → Add their subject marks
3. Press `2` → View their GPA
4. Press `3` → Generate a report

---

## How Data is Saved

All student records are stored in `students_data.py` as a Python list:

```python
students = [
    {'id': 1003, 'name': 'Shreya Tripathi', 'grades': {'chemistry': 100, 'mathematics': 100, 'programming': 100}},
    ]
```

Every add or delete updates this file automatically.

---

## GPA Scale

| Marks Average | GPA   | Grade            |
|---------------|-------|------------------|
| 90 – 100      | 9–10  | O (Outstanding)  |
| 80 – 89       | 8–8.9 | A+ (Excellent)   |
| 70 – 79       | 7–7.9 | A (Very Good)    |
| 60 – 69       | 6–6.9 | B+ (Good)        |
| 50 – 59       | 5–5.9 | B (Average)      |
| 40 – 49       | 4–4.9 | C (Pass)         |
| Below 40      | <4    | F (Fail)         |
