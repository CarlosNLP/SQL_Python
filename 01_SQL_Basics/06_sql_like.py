import sqlite3

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Table name: players
# Columns/Fields: Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves
# Total: 491 players/entries/rows (sorted by Overall)

# Selecting all the data and fetching all
cur.execute("SELECT * FROM players WHERE Name LIKE '%ar%'") # selecting all the players whose name contains 'ar' anywhere
rows = cur.fetchall()
print("SELECT * FROM players WHERE Name LIKE '%ar%'")
print('Number of filtered players:', len(rows), '\n')

# Displaying some of the entries for reference
print(rows[:5])

# Closing database connection
cur.close()
conn.close()
