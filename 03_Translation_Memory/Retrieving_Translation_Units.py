import sqlite3 # library to handle databases with SQLite
import re # library to apply regular expressions

# TIP:
# To dump the translation units into a text file automatically, open the console in this directory and execute:
# Retrieving_Translation_Units.py > all.txt
# All the translation units will be dumped into the all.txt file, source and target separated by a tabulator

# Connecting to our database
db_path = 'database/Studio_TM_GitHub.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Retrieving the translation units
cur.execute('SELECT source_segment, target_segment from translation_units')
rows = cur.fetchall()

# Going through each translation unit, each row will be a tuple consisting of (source_segment, target_segment)
for row in rows:
    source_segment = row[0] # 0th indexed element of the tuple: source_segment
    matches = re.findall(r"(<Value[^>]*?>.*?</Value>|<TagID[^>]*?>.*?</TagID>)", source_segment) # getting the text and the tags with a regular expression
    matches = [match.replace('<TagID>', '{TagID_') for match in matches] # transforming the opening tag into a placeholder
    matches = [match.replace('</TagID>', '}') for match in matches] # transforming the closing tag into a placeholder
    matches = [re.sub('<[^>]+?>', '', match) for match in matches] # removing all the remaining markup
    print("".join(matches), end='\t') # printing all the matches together to build the whole source segment
    
    target_segment = row[1] # 1st indexed element of the tuple: target_segment
    matches = re.findall(r"(<Value[^>]*?>.*?</Value>|<TagID[^>]*?>.*?</TagID>)", target_segment) # getting the text and the tags with a regular expression
    matches = [match.replace('<TagID>', '{TagID_') for match in matches] # transforming the opening tag into a placeholder
    matches = [match.replace('</TagID>', '}') for match in matches] # transforming the closing tag into a placeholder
    matches = [re.sub('<[^>]+?>', '', match) for match in matches] # removing all the remaining markup
    print("".join(matches)) # printing all the matches together to build the whole target segment

# Closing database connection
cur.close()
conn.close()
