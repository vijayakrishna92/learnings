import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')
# CREATE TABLE, IF, NOT, EXISTS, INTEGER, PRIMARY, KEY, AUTOINCREMENT, TEXT, INSERT, INTO, VALUES these are all SQL keywords.
# students is the name of the table, id is the primary key, name is a text field, and age is an integer.

# AUTOINCREMENT is used to automatically increment the id for each new record.

# Insert sample data
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 21)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 23)")


# Save and close
conn.commit()
conn.close()

print("✅ Database created and data inserted.")