# University Student Management System

This is a Python-based university student management system that utilizes a MySQL database for persistent storage. The project provides functionality to manage student records, including insertion, deletion, search, and analysis.

## Features

- Add new students with multiple courses and grades
- Automatically calculate and store GPA
- Search students by ID
- View all student records
- Delete student records
- Count total students
- Display average GPA of the university
- Show students with GPA higher than the university average

## Technologies Used

- **Python 3**
- **MySQL** (tested with MySQL 8+)
- **PyMySQL** for database connectivity
- Object-Oriented Programming (OOP)

## Setup Instructions

1. **Install MySQL** and create a database
2. Run the program

# Notes

GPA is automatically calculated and stored when inserting a student.

Deleting a student will also remove their course records.

The system prevents duplicate IDs and invalid grades (must be between 0 and 20).

---

Author: Mohammad Arshia Jafari
