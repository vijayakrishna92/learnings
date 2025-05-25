import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("📄 All Students:")
for row in rows:
    print(row)

conn.close()

# SELECT name FROM students;
#SELECT * FROM students WHERE age > 21; reurns all columns for students older than 21.
# SELECT * FROM students ORDER BY age DESC; # returns all columns for students ordered by age in descending order.
# SELECT * FROM students LIMIT 1; # returns the first student. 1 st row
#INSERT INTO students (name, age) VALUES ('John', 24); # inserts a new student named John with age 24.
# UPDATE students SET age = 22 WHERE name = 'Alice'; # updates Alice's age to 22.
# DELETE FROM students WHERE name = 'Bob'; # deletes the student named Bob.
# SELECT COUNT(*) FROM students; # returns the total number of students.
# SELECT AVG(age) FROM students; # returns the average age of all students.
# SELECT name FROM students WHERE age BETWEEN 20 AND 25; # returns names of students whose age is between 20 and 25.
# SELECT * FROM students WHERE name LIKE 'A%'; # returns all students whose name starts with 'A'.
# SELECT * FROM students WHERE age IN (21, 23); # returns all students whose age is either 21 or 23.
# SELECT age, COUNT(*) FROM students GROUP BY age; # returns the count of students grouped by age.
'''
SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id;
'''# This query retrieves the names of students along with their grades by joining the students and grades tables on the student ID.
# SELECT name FROM students
#WHERE age = (SELECT MAX(age) FROM students); # This query retrieves the name of the oldest student by using a subquery to find the maximum age in the students table.