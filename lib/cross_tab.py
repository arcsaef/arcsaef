import json
import re
import sys
import sqlite3

# Crosstab: AI, CI PI, publication count over the years

# Example usage:
# python3 lib/cross_tab.py data/all/BIB_saef_20250401.json data/all/saef_library.db

# Export item > BetterBibTex JSON
with open(sys.argv[1], 'r') as f:
    bib = json.load(f)

# prepare temporary tables
sqliteConnection = sqlite3.connect(sys.argv[2])
cursor_obj = sqliteConnection.cursor()

# Drop the tmp_outputs_basic table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS tmp_outputs_author")

# Creating table
table = ''' CREATE TABLE tmp_outputs_author (
            pub_id TEXT NOT NULL,
            pub_yr INTEGER NOT NULL,
            title TEXT NOT NULL,
            author_key TEXT NOT NULL
        ); '''

cursor_obj.execute(table)
print("Table - tmp_outputs_author,  is Ready")

# publication key, publication year, publication title
for b in bib['items']:
    if b['itemType'] == 'journalArticle':
        pubyr = ''.join(re.findall( '\d{4}', b['date'])) 
        saef_author_list    = re.findall('saef:.*', b['extra']) 

        for names in saef_author_list:
            names_tidy  = re.sub('saef:', '', names, flags=re.IGNORECASE)
            names_split = names_tidy.strip().split(';') # Create a list of saef names

            for name in names_split:
                insert_query =  '''
                    INSERT INTO tmp_outputs_author (pub_id, pub_yr, title, author_key ) 
                    VALUES (?, ?, ?, ?);
                    '''
                row_data = (b['itemKey'], pubyr, b['title'], name.strip())
                cursor_obj.execute(insert_query, row_data)

# Commit your changes in the database     
sqliteConnection.commit() 

# ToDo add itemType: book & bookChapter

# Closing the connection 
if sqliteConnection:
  sqliteConnection.close()
