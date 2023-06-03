import sqlite3
#Scroll down to manage database

# Database Creation
def create_database():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)''')
    conn.commit()
    conn.close()

# Data Manipulation
def insert_student(name, age, email):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    conn.close()

def update_student_age(student_id, new_age):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

# Data Retrieval
def retrieve_all_students():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    students = []
    for row in rows:
        student = {'id': row[0], 'name': row[1], 'age': row[2], 'email': row[3]}
        students.append(student)
    conn.close()
    return students

def retrieve_student_by_id(student_id):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = c.fetchone()
    if row is None:
        return None
    student = {'id': row[0], 'name': row[1], 'age': row[2], 'email': row[3]}
    conn.close()
    return student

# Querying
def get_average_age():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT AVG(age) FROM students")
    average_age = c.fetchone()[0]
    conn.close()
    return average_age

def get_student_count():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM students")
    count = c.fetchone()[0]
    conn.close()
    return count

# Main program (you can use the database from here)
if __name__ == '__main__':
    create_database()

    insert_student('Berkay Oğuzhan', 20, 'berkay@example.com')
    insert_student('James Hetfield', 54, 'james@example.com')

    update_student_age(1, 21)

    delete_student(2)

    all_students = retrieve_all_students()
    print("All Students:")
    for student in all_students:
        print(student)

    student = retrieve_student_by_id(2)
    print("\nStudent with ID :")
    print(student)

    average_age = get_average_age()
    print("\nAverage Age of Students:", average_age)

    student_count = get_student_count()
    print("Number of Students:", student_count)