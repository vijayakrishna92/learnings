CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
);

INSERT INTO students (name, age) VALUES ('Alice', 21);
INSERT INTO students (name, age) VALUES ('Bob', 23);

SELECT * FROM students;
-- to run this script, use the following commands in your terminal:sqlite3 mydb.db < create_insert.sql 
/* multi line comment */
-- This is a single-line comment
/* mysql -u user -p mydb < script.sql
psql -U user -d mydb -f script.sql
Those are commands for running SQL scripts using MySQL and PostgreSQL command-line tools.
*/