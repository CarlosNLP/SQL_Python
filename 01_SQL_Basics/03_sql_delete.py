import sqlite3

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Table name: players
# Columns/Fields: Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves

cur.execute('SELECT * FROM players') # selecting all the players
rows = cur.fetchall()
print('Number of total players:', len(rows))

# Removing the CarlosNLP player our database
cur.execute("DELETE FROM players WHERE Name = 'CarlosNLP'") # removing a specific player from our database

# Committing the change into the database
conn.commit()

cur.execute('SELECT * FROM players') # selecting all the players
rows = cur.fetchall()
# Getting the number of players to make sure our fake player was deleted
print('Number of total players:', len(rows))

# Closing database connection
cur.close()
conn.close()
