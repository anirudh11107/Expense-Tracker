# Student Bio Management System

This Python program allows you to manage student details stored in a CSV file (`Student_data.csv`). It provides a simple menu-driven interface to add new student data, read existing records, search by admission number, find students with maximum and minimum CGPA scores, and display students with high CGPA. The project is ideal for learning file handling, basic data validation, and simple data analysis using Python.

---

## Table of Contents

- Overview  
- Features  
- Project Structure  
- Data Fields  
- How to Use  
- Sample Workflow  
- Error Handling & Validation  
- Pre-requisites  
- Limitations & Future Enhancements  
- Educational Objectives  
- Author  
- License  

---

## Overview

The Student Records Management System is a console-based application built using Python and the standard `csv` module. It uses a CSV file as persistent storage, making it easy to open and inspect the data in spreadsheet applications like Excel or Google Sheets. The program is designed to be beginner-friendly while demonstrating good coding practices such as modular functions and clean separation of concerns.

---

## Features

- Add student records with the following fields:
  - Admission Number  
  - Name  
  - Age  
  - Grade  
  - Section  
  - City  
  - State  
  - Mother Tongue  
  - CGPA Score  

- Read and display all student records from `Student_data.csv`.  
- Search for a student by Admission Number (unique identifier).  
- Find student(s) with the maximum CGPA score.  
- Find student(s) with the minimum CGPA score.  
- Display all students having CGPA score greater than or equal to 9.0.  
- Data validation and basic error handling for robust operations.  
- Automatic creation of the CSV file (with headers) if it does not exist when inserting data.

---

## Project Structure

A typical structure for this project can be:

student-records-project/
│
├─ student_records.py # Main Python script with all functions and menu
├─ Student_data.csv # CSV file storing student records (created at runtime)
└─ README.md # Project documentation (this file)


You can rename `student_records.py` if needed, but be sure to update references in your documentation or report.

---

## Data Fields

Each student record in `Student_data.csv` contains the following columns:

1. `Admn_no` – Admission Number (integer, should be unique per student)  
2. `Name` – Full name of the student (string)  
3. `Age` – Age in years (integer)  
4. `Grade` – Academic grade/standard (integer, e.g., 8, 9, 10, 11, 12)  
5. `Section` – Class section (string, e.g., A, B, C)  
6. `City` – City of residence (string)  
7. `State` – State or region (string)  
8. `Mother_Tongue` – Primary or native language (string)  
9. `CGPA_Score` – CGPA on a 0.0–10.0 scale (float)

This tabular structure makes it easy to filter, sort, and analyze data later using other tools if required.

---

## How to Use

1. Make sure `student_records.py` and (optionally) `Student_data.csv` are in the same folder.  
2. Open a terminal or command prompt in that folder.  
3. Run the script:  
4. A menu will be displayed with options similar to:

--- Student Records Management ---

Read CSV file

Add new student data

Search by Admission number

Show student(s) with maximum CGPA score

Show student(s) with minimum CGPA score

Display students with CGPA >= 9

Exit

5. Enter the number corresponding to the operation you want to perform.  
6. Follow the on-screen prompts to provide input where required (e.g., when adding a student or searching).

---

## Sample Workflow

Example: Adding a new student and then searching for them.

1. Choose option `2` (Add new student data).  
2. Enter details when prompted, for example:
Enter Admission number (numeric): 101
Enter Name: Rahul Sharma
Enter age (years): 16
Enter Grade (numeric): 11
Enter section: B
Enter City: Mumbai
Enter State: Maharashtra
Enter Mother Tongue: Hindi
Enter CGPA score (0.0 - 10.0): 9.2
Add more data? (y/n): n
3. Choose option `1` to read and display all records and confirm that the new student is saved.  
4. Choose option `3` and enter `101` to search specifically by admission number.  
5. Choose option `4` or `6` to see if this student appears in maximum/high CGPA lists, depending on the data.

---

## Error Handling & Validation

The program includes basic input validation and error handling such as:

- Ensuring Admission Number is numeric.  
- Ensuring Age and Grade are numeric.  
- Ensuring CGPA is numeric and in the range 0.0 to 10.0.  
- Handling the case when the CSV file does not exist (it will be created on first write).  
- Displaying friendly messages when:
- A searched Admission Number is not found.  
- The file is empty or there are no records matching the criteria (e.g., no student with CGPA ≥ 9.0).

If invalid input is entered (like letters where a number is expected), the program will show an error message and ask for the data again.

---

## Pre-requisites

- Python 3.x installed on your computer.  
- The standard `csv` module (this comes pre-installed with Python).  
- A terminal or command prompt to run the script.

No external libraries are required, so the setup is very lightweight.

---

## Limitations & Future Enhancements

Current limitations:

- Uses a CSV file instead of a full database, so it is more suited for small to medium datasets.  
- All operations are performed through a text-based CLI.  
- No authentication or user roles (e.g., admin, teacher, student).

Possible future enhancements:

- Add sorting and filtering options (e.g., sort by CGPA, list students by city, etc.).  
- Add update and delete operations for existing student records.  
- Convert the project into a GUI application using libraries like Tkinter or PyQt.  
- Migrate data storage from CSV to a database system (SQLite, MySQL, etc.) for better scalability.  
- Add report generation (PDF/Excel) for summaries like class-wise toppers, city-wise distribution, etc.

---

## Educational Objectives

This project is especially useful for students learning:

- Python file handling (`open`, read, write, append).  
- Working with the `csv` module for structured data storage.  
- Using loops, conditionals, and functions to build a menu-driven application.  
- Basic data validation and defensive programming.  
- Organizing code into logical functions for readability and reuse.

Teachers can also use this as a practical assignment to reinforce concepts of file handling and simple data processing.

---

## Author

[Your Name]  
Class / Institution (optional)  
Email: your.email@example.com (optional)  

Feel free to customize this section with your real details for submissions or portfolios.

---

## License

This is an open-source project licensed under the MIT License.  
You are free to use, modify, and distribute this code, provided that proper credit is given to the original author and the license terms are followed.

