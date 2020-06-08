import sqlite3
import random

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Creating testing table if it doesn't exist
cur.execute("""CREATE TABLE IF NOT EXISTS "testing_players" (
                    "Name"	TEXT,
                    "Age"	INTEGER,
                    "Nationality"	TEXT,
                    "Overall"	INTEGER,
                    "Club"	TEXT,
                    "Value"	INTEGER,
                    "Wage"	INTEGER,
                    "PreferredFoot"	TEXT,
                    "WeakFoot"	INTEGER,
                    "SkillMoves"	INTEGER
                    );""")

# Getting the table names available in our database
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall() # this bring us a list of tables

# Looping through the tables
for table in tables:
    print('Table name:', table[0]) # using [0] because the name itself is the first element of the tuple

# Deleting testing table if it exists
cur.execute("DROP TABLE IF EXISTS 'testing_players'")

# Closing database connection
cur.close()
conn.close()
