import sqlite3

connection = sqlite3.connect("database.db")

connection.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    fullname VARCHAR(255),
    email VARCHAR(50) UNIQUE
)''')

try:
    connection.execute('''INSERT INTO users (fullname,userid,email)
VALUES ("Diyorbek Torabekov", 2008,"DiyorbekTorabekov@gmail.com")''')
    print("Successfully created")
except:
    print("Error")




connection.commit()
connection.close()
