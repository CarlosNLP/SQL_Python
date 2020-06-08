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
print('Number of total players:', len(rows))

# Inserting a player into our database
##cur.execute("""INSERT INTO players (Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves)
##               VALUES ('CarlosNLP', 27, 'Spain', 85, 'Python FC', 50, 30, 'Right', 4, 4)""") # inserting a player with all the fields from our database

# If the number of fields is the same as the number of values added, we can skip the field names as per below
cur.execute("""INSERT INTO players
               VALUES ('CarlosNLP', 27, 'Spain', 85, 'Python FC', 50, 30, 'Right', 4, 4)""") # inserting a player with all the fields from our database

# Committing the change into the database
conn.commit()

cur.execute('SELECT * FROM players') # selecting all the players
rows = cur.fetchall()
# Getting the number of players to make sure our fake player was added
print('Number of total players:', len(rows))

# Showing the entry from the added player
print(rows[-1])

# Closing database connection
cur.close()
conn.close()
