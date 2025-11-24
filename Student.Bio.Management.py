import csv

FILE_NAME = 'Student_data.csv'
FIELDS = ['Admn_no', 'Name', 'Age', 'Grade', 'Section', 'City', 'State', 'Mother_Tongue', 'CGPA_Score']

def read_csv_file():
    """Read and display data from the CSV file"""
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            fobj = csv.reader(f)
            rows = list(fobj)
            if not rows:
                print("File is empty.")
                return
            print(f"{' | '.join(FIELDS)}")
            print("-" * 80)
            for row in rows:
                print(' | '.join(row))
    except FileNotFoundError:
        print(f"No file named '{FILE_NAME}' found. Please create the file first.")

def write_csv_file():
    """Append new student records to the CSV file"""
    try:
        # Check if file exists - if not, create and write headers
        try:
            with open(FILE_NAME, 'r', newline='') as f:
                pass
        except FileNotFoundError:
            with open(FILE_NAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(FIELDS)

        with open(FILE_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            while True:
                try:
                    admn_no = int(input('Enter Admission number (numeric): '))
                    name = input('Enter Name: ').strip()
                    age = int(input('Enter age (years): '))
                    grade = int(input('Enter Grade (numeric): '))
                    section = input('Enter section: ').strip()
                    city = input('Enter City: ').strip()
                    state = input('Enter State: ').strip()
                    mother_tongue = input('Enter Mother Tongue: ').strip()
                    cgpa_score = float(input('Enter CGPA score (0.0 - 10.0): '))
                    if not (0 <= cgpa_score <= 10):
                        print("CGPA score should be between 0 and 10.")
                        continue
                    data = [admn_no, name, age, grade, section, city, state, mother_tongue, cgpa_score]
                    writer.writerow(data)
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
                    continue
                more = input('Add more data? (y/n): ').strip().lower()
                if more != 'y':
                    break
        print('Data added successfully.')
    except Exception as e:
        print(f"An error occurred: {e}")

def search_csv_file():
    """Search student details by Admission number"""
    try:
        admn_no = int(input('Enter Admission number to search: '))
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.DictReader(f)
            found = False
            for row in reader:
                if int(row['Admn_no']) == admn_no:
                    print("Student details found:")
                    for field in FIELDS:
                        print(f"{field}: {row[field]}")
                    found = True
                    break
            if not found:
                print("Admission number not found.")
    except FileNotFoundError:
        print(f"No file named '{FILE_NAME}' found.")
    except ValueError:
        print("Please enter a valid numeric Admission number.")

def max_csv_file():
    """Display student(s) with maximum CGPA score"""
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.DictReader(f)
            max_cgpa = -1.0
            max_students = []
            for row in reader:
                try:
                    cgpa = float(row['CGPA_Score'])
                    if cgpa > max_cgpa:
                        max_cgpa = cgpa
                        max_students = [row]
                    elif cgpa == max_cgpa:
                        max_students.append(row)
                except ValueError:
                    continue
            if max_students:
                print(f"Student(s) with maximum CGPA score: {max_cgpa}")
                for student in max_students:
                    print({field: student[field] for field in FIELDS})
            else:
                print("No students found in the file.")
    except FileNotFoundError:
        print(f"No file named '{FILE_NAME}' found.")

def min_csv_file():
    """Display student(s) with minimum CGPA score"""
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.DictReader(f)
            min_cgpa = 11.0
            min_students = []
            for row in reader:
                try:
                    cgpa = float(row['CGPA_Score'])
                    if cgpa < min_cgpa:
                        min_cgpa = cgpa
                        min_students = [row]
                    elif cgpa == min_cgpa:
                        min_students.append(row)
                except ValueError:
                    continue
            if min_students:
                print(f"Student(s) with minimum CGPA score: {min_cgpa}")
                for student in min_students:
                    print({field: student[field] for field in FIELDS})
            else:
                print("No students found in the file.")
    except FileNotFoundError:
        print(f"No file named '{FILE_NAME}' found.")

def display_high_cgpa(threshold=9.0):
    """Display students with CGPA score greater than or equal to threshold"""
    try:
        with open(FILE_NAME, 'r', newline='') as f:
            reader = csv.DictReader(f)
            print(f"Students with CGPA >= {threshold}:")
            found = False
            for row in reader:
                try:
                    cgpa = float(row['CGPA_Score'])
                    if cgpa >= threshold:
                        print({field: row[field] for field in FIELDS})
                        found = True
                except ValueError:
                    continue
            if not found:
                print(f"No students with CGPA >= {threshold} found.")
    except FileNotFoundError:
        print(f"No file named '{FILE_NAME}' found.")

def main():
    options = {
        1: ('Read CSV file', read_csv_file),
        2: ('Add new student data', write_csv_file),
        3: ('Search by Admission number', search_csv_file),
        4: ('Show student(s) with maximum CGPA score', max_csv_file),
        5: ('Show student(s) with minimum CGPA score', min_csv_file),
        6: ('Display students with CGPA >= 9', display_high_cgpa),
        7: ('Exit', None)
    }

    while True:
        print('\n--- Student Records Management ---')
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice not in options:
            print("Invalid choice. Try again.")
            continue
        if choice == 7:
            print('Thank you for using the program. Have a nice day!')
            break

        func = options[choice][1]
        if func:
            func()

if __name__ == "__main__":
    main()
