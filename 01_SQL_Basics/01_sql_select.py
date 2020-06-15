import sqlite3

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Table name: players
# Columns/Fields: Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves
# Total: 491 players/entries/rows (sorted by Overall)

# Selecting all the data and fetching all
cur.execute("SELECT * FROM players") # selecting all the players
rows = cur.fetchall()
print('SQL query: SELECT * FROM players')
print('Number of total players:', len(rows), '\n')

# Selecting data with specific condition and fetching all
cur.execute("SELECT * FROM players WHERE Nationality = 'Spain'") # selecting all the Spanish players
rows = cur.fetchall()
print("SQL query: SELECT * FROM players WHERE Nationality = 'Spain'")
print('Number of Spanish players:', len(rows), '\n')

# Selecting data with several conditions and fetching all
cur.execute("SELECT * FROM players WHERE Nationality = 'Spain' AND Club = 'Real Madrid'") # selecting all the Spanish players in Real Madrid
rows = cur.fetchall()
print("SQL query: SELECT * FROM players WHERE Nationality = 'Spain' AND Club = 'Real Madrid'")
print('Number of Spanish players in Real Madrid:', len(rows), '\n')

# Retrieving the rows from the table after applying a query, and confirming the result is a list of tuples
print('rows:', type(rows))
print('rows[0]:', type(rows[0]))

# Printing the rows list for reference
print(rows)

# Printing just the first element of the rows list, which is a tuple
print(rows[0])

# So if we wanted to retrieve the name of the first player, for example, we would do the following:
print(rows[0][0]) # because the Name field is the first element of the tuple

# Closing database connection
cur.close()
conn.close()
