# Select a random game and print all of the categories from that game
import sqlite3
from html.parser import HTMLParser

connection = sqlite3.connect("./data/jeopardy.db")
cursor = connection.cursor()

query_1 = """SELECT game 
             FROM category 
             ORDER BY RANDOM() 
             LIMIT 1"""

cursor.execute(query_1)
results = cursor.fetchall()
game_id = results[0][0]

print("\nCategories for game #%d:\n" % (game_id,))

query_2 = """SELECT name, round 
             FROM category
             WHERE game = %d 
             ORDER BY round""" % (game_id,)

cursor.execute(query_2)
results = cursor.fetchall()

p = HTMLParser()

for row in results:
    # round 0 = Jeopardy round
    # round 1 = Double Jeopardy
    # round 2 = Final Jeopardy
    name, round = row
    print("Round %d: %s" % (round, p.unescape(name)))

connection.close()

