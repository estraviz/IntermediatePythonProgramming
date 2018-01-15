# Print value, question and answer for 10 Jeopardy clues
import sqlite3
from html.parser import HTMLParser

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()
cursor.execute("SELECT text, answer, value FROM clue LIMIT 10;")
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

