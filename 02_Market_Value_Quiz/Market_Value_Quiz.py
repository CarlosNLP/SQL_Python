import sqlite3
import random

# Path and opening database
db_path = "database/fifa2019_players.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Selecting all the data and fetching all
cur.execute("SELECT * FROM players") # actually, we will just be using Name and Value so we could say 'SELECT Name, Value FROM players', but that's okay
rows = cur.fetchall()

# Name, Age, Nationality, Overall, Club, Value, Wage, PreferredFoot, WeakFoot, SkillMoves
# rows = list, row = tuple, total = 491 players

# Method to retrieve the player name
def get_name(row):
    name = row[0]
    return name

# Method to retrieve the player value
def get_value(row):
    value = row[5]
    return value

print('Welcome to the Market Value Quiz for FIFA 19')
print("Rules: enter '+', '-' or '='\n")

# Initial value for the points
points = 0

# Generate number 1
row_number1 = random.choice([n for n in range(0, 491)])

# Retrieving player 1
player_name1 = get_name(rows[row_number1])
player_value1 = get_value(rows[row_number1])
print(player_name1 + ":", str(player_value1) + "M")

while True: # keep playing until the input is wrong
    # Generate number 2 which will be different to number 1
    row_number2 = random.choice([n for n in range(0, 491) if n != row_number1])
    
    # Retrieving player 2
    player_name2 = get_name(rows[row_number2])
    player_value2 = get_value(rows[row_number2])
    player_value2_input = input(player_name2 + ": ")
    
    # Code block handling the user input
    if player_value2_input == "+":
        if player_value2 > player_value1: # correct input
            points += 1
            print('Correct! %s point(s).\n' % (points))
            print(player_name2 + ":", str(player_value2) + "M")
        else: # wrong input
            print("\nWrong!", player_name2 + ":", str(player_value2) + "M")
            print('%s point(s)' % (points))
            input('Press Enter to exit.')
            break
    elif player_value2_input == "-":
        if player_value2 < player_value1: # correct input
            points += 1
            print('Correct! %s point(s).\n' % (points))
            print(player_name2 + ":", str(player_value2) + "M")
        else: # wrong input
            print("\nWrong!", player_name2 + ":", str(player_value2) + "M")
            print('%s point(s)' % (points))
            input('Press Enter to exit.')
            break
    elif player_value2_input == "=":
        if player_value2 == player_value1: # correct input
            points += 1
            print('Correct! %s point(s).\n' % (points))
            print(player_name2 + ":", str(player_value2) + "M")
        else: # wrong input
            print("\nWrong!", player_name2 + ":", str(player_value2) + "M")
            print('%s point(s)' % (points))
            input('Press Enter to exit.')
            break
    else: # invalid input
        print('Game over. Points: %s' % (points))
        input('Press Enter to exit.')
        break
    
    # Excluding current row number for next round - player 1 becomes the same as player 2, and we'll pick a new player 2
    row_number1 = row_number2
    player_value1 = player_value2

# Closing database connection
cur.close()
conn.close()
