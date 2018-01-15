# Print value, question and answer for Jeopardy clues from a random category
import sqlite3
from html.parser import HTMLParser

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

query_1 = """SELECT id, name 
             FROM category 
             ORDER BY RANDOM() 
             LIMIT 1"""

cursor.execute(query_1)
results = cursor.fetchall()

category_id, name = results[0]

print("\nCategory %s:" % (category_id,))

query_2 = """SELECT text, answer, value  
             FROM clue
             WHERE category = %d 
             ORDER BY value""" % (category_id,)

cursor.execute(query_2)
results = cursor.fetchall()

p = HTMLParser()

for clue in results:
    text, answer, value = clue
    print("\n[$%s]" % (value,))
    print("Question: %s" % (p.unescape(text),))
    print("Answer: What is '%s'?" % (p.unescape(answer),))
else:
    print("\n")

connection.close()

