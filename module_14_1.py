import sqlite3
import random

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance  INTEGER
    )
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (f'User{i+1}', f'example{i+1}@gmail.com', 10*(i+1), 1000))
# cursor.execute("UPDATE Users SET balance=? WHERE id%2==?", (500, 1))
# cursor.execute("DELETE FROM Users WHERE id%3==?",(1,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age!=?", (60,))
users = cursor.fetchall()
for user in users:
    s = ""
    for i in user:
        s = s + str(i) + "|"
    print(s[0:-1])

connection.commit()
connection.close()
