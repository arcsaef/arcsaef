import json
import re
import sys
import sqlite3

# Crosstab: AI, CI PI, publication count over the years

# Export item > BetterBibTex JSON
with open(sys.argv[1], 'r') as f:
    bib = json.load(f)

# prepare temporary tables
sqliteConnection = sqlite3.connect(sys.argv[2])
cursor_obj = sqliteConnection.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS tmp_outputs_basic")

# Creating table
table = ''' CREATE TABLE tmp_outputs_basic (
            key TEXT NOT NULL,
            pubyr INTEGER NOT NULL,
            title TEXT NOT NULL
        ); '''

cursor_obj.execute(table)
print("Table - tmp_outputs_basic,  is Ready")

# publication key, publication year, publication title
for b in bib['items']:
    if b['itemType'] == 'journalArticle':
        pubyr = ''.join(re.findall( '\d{4}', b['date'])) 
        insert_query =  '''
            INSERT INTO tmp_outputs_basic (key, pubyr, title ) 
            VALUES (?, ?, ?);
            '''
        row_data = (b['key'], pubyr, b['title'])
        cursor_obj.execute(insert_query, row_data)

# Commit your changes in the database     
sqliteConnection.commit() 
  
# Closing the connection 
if sqliteConnection:
  sqliteConnection.close()
