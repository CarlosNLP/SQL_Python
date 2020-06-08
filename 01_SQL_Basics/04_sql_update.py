import sqlite3
import random

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Table name: players
# Columns/Fields: Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves

cur.execute('SELECT * FROM players') # selecting all the players
rows = cur.fetchall()
# Getting the Name and Age of the last player
print('Name:', rows[-1][0], 'Age:', rows[-1][1]) # [-1] means the last entry from the list, and [0] and [1] are Name and Age, respectively

# Updating Age for the player CarlosNLP (you need to add the player first using 02_sql_insert.py)
cur.execute("UPDATE players SET Age = 25 WHERE Name = 'CarlosNLP'")

# Committing the change into the database
conn.commit()

cur.execute('SELECT * FROM players') # selecting all the players
rows = cur.fetchall()
# Getting the Name and Age of the last player to make sure it has been updated
print('Name:', rows[-1][0], 'Age:', rows[-1][1]) # [-1] means the last entry from the list, and [0] and [1] are Name and Age, respectively

# Closing database connection
cur.close()
conn.close()
