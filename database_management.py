import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Creation of names table in database
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL)
# """)

cursor.execute("""
SELECT * FROM users
""")

res = cursor.fetchall()

print(res)





