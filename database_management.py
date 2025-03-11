import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM users
""")

connection.commit()
result = cursor.fetchall()
connection.close()

print(result)