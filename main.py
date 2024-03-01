import sqlite3

connection = sqlite3.connect("database.db")

connection.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NULL,
    email TEXT NULL,
    phone TEXT NULL
)
''')



connection.execute('''INSERT INTO users (first_name, last_name, email,phone)
VALUES ("Diyorbek", "Torabekov", "Diyorbek@gmail.com", "0712345678")''')

connection.commit()
connection.close()