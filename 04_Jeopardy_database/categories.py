# Print the names of 10 Jeopardy categories
import sqlite3

connection = sqlite3.connect("./data/jeopardy.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM category LIMIT 10;")
results = cursor.fetchall()

for category in results:
    print(category[0])

connection.close()

