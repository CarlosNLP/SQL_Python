import sqlite3 # library to handle databases with SQLite

# Connecting to our database
db_path = 'database/Studio_TM_GitHub.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Retrieving the name, source and target languages, and the creation user under the table named 'translation_memories'
cur.execute('SELECT name, source_language, target_language, creation_user from translation_memories')
rows = cur.fetchall()

# NOTE: under the translation_memories table, we would see an entry per TM. However, Studio TMs are bilingual so we'll just see one entry (first ID)
studioTM = rows[0] # getting the Studio TM (first ID/entry)
name = studioTM[0] # 1st field/column (0th indexed)
source_language = studioTM[1] # 2nd field/column (0th indexed)
target_language = studioTM[2] # 3rd field/column (0th indexed)
creation_user = studioTM[3] # 4th field/column (0th indexed)

print('TM name:', name)
print('Source language:', source_language)
print('Target language:', target_language)
print('TM creation user:', creation_user)

# Retrieving the number of translation units
cur.execute('SELECT name, seq from sqlite_sequence')
rows = cur.fetchall()

# NOTE: under the sqlite_sequence table, we will see the number of translation memories, attributes and translation units (one per row/entry)
for row in rows: # looping through the rows/entries
    if row[0] == 'translation_units':
        translation_units = row[1] # getting the number, which can be found in the second field (0th indexed) of the search ('seq' field)

print('Number of translation units:', translation_units)

# Closing database connection
cur.close()
conn.close()
