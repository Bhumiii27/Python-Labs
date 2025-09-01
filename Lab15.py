import sqlite3

conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        Enrollment INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_subject (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Enrollment INTEGER,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL,
        FOREIGN KEY (Enrollment) REFERENCES student(Enrollment)
    )
''')

students = [
    (92301733016, 'ASHUTOSH KUMAR SINGH'),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI'),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA'),
    (92301733046, 'SHIVAM ATULKUMAR BHATT'),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA')
]

try:
    cursor.executemany('INSERT INTO student (Enrollment, name) VALUES (?, ?)', students)
except sqlite3.IntegrityError:
    pass

subjects = [
    (92301733016, 'PWP', 95),
    (92301733016, 'Math', 88),
    (92301733017, 'PWP', 85),
    (92301733017, 'Physics', 82),
    (92301733027, 'PWP', 90),
    (92301733046, 'PWP', 93),
    (92301733058, 'PWP', 75),
    (92301733058, 'Math', 80)
]

try:
    cursor.executemany('''
        INSERT INTO student_subject (Enrollment, Subject, Mark) 
        VALUES (?, ?, ?)
    ''', subjects)
except sqlite3.IntegrityError:
    pass

conn.commit()

cursor.execute('''
    SELECT student.Enrollment, student.name, student_subject.Subject, student_subject.Mark
    FROM student
    JOIN student_subject ON student.Enrollment = student_subject.Enrollment
''')
records = cursor.fetchall()
print("All Student Records with Subjects:")
for row in records:
    print(row)

cursor.execute('''
    SELECT student.name, student_subject.Subject, student_subject.Mark
    FROM student
    JOIN student_subject ON student.Enrollment = student_subject.Enrollment
    WHERE student_subject.Mark > 90
''')
high_scores = cursor.fetchall()
print("\nStudents with Marks > 90:")
for record in high_scores:
    print(record)

cursor.execute('''
    UPDATE student_subject
    SET Mark = 98
    WHERE Enrollment = 92301733016 AND Subject = 'PWP'
''')
conn.commit()

cursor.execute('''
    SELECT student.name, student_subject.Mark
    FROM student
    JOIN student_subject ON student.Enrollment = student_subject.Enrollment
    WHERE student.name = 'ASHUTOSH KUMAR SINGH' AND student_subject.Subject = 'PWP'
''')
updated = cursor.fetchone()
print(f"\nUpdated mark for {updated[0]} in PWP: {updated[1]}")

cursor.execute('''
    DELETE FROM student_subject
    WHERE Enrollment = 92301733058 AND Subject = 'PWP'
''')
conn.commit()

cursor.execute('''
    SELECT * FROM student_subject
    WHERE Enrollment = 92301733058 AND Subject = 'PWP'
''')
if cursor.fetchone() is None:
    print("\nRecord for DEVENDRASINH DOLATSINH JADEJA in PWP has been successfully deleted.")

cursor.execute('SELECT AVG(Mark) FROM student_subject')
avg = cursor.fetchone()[0]
print(f"\nAverage mark across all subjects: {avg:.2f}")

conn.close()
