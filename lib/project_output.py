import json
import re
import sys
import sqlite3

# Example usage:
# python3 lib/cross_tab.py data/all/BIB_saef_20250401.json data/all/saef_library.db

# Export item > BetterBibTex JSON
with open(sys.argv[1], 'r') as f:
    bib = json.load(f)

# prepare temporary tables
sqliteConnection = sqlite3.connect(sys.argv[2])
cursor_obj = sqliteConnection.cursor()

# Drop the outputs_project table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS output_project")

# Creating table
table = ''' CREATE TABLE output_project (
            pub_id TEXT NOT NULL,
            pub_yr INTEGER NOT NULL,
            title TEXT NOT NULL,
            project_id TEXT NOT NULL
        ); '''

cursor_obj.execute(table)
print("Table - output_project,  is Ready")

# publication key, publication year, publication title, project id
for b in bib['items']:
    if b['itemType'] == 'journalArticle':
        pubyr = ''.join(re.findall( '\d{4}', b['date'])) 
        saef_project_list    = re.findall('project:.*', b['extra']) 

        for names in saef_project_list:
            names_tidy  = re.sub('project:', '', names, flags=re.IGNORECASE)
            names_split = names_tidy.strip().split(';') # Create a list of saef projects

            for name in names_split:
                insert_query =  '''
                    INSERT INTO output_project (pub_id, pub_yr, title, project_id ) 
                    VALUES (?, ?, ?, ?);
                    '''
                row_data = (b['itemKey'], pubyr, b['title'], name.strip())
                cursor_obj.execute(insert_query, row_data)

# Commit your changes in the database     
sqliteConnection.commit() 
      
# Closing the connection 
if sqliteConnection:
  sqliteConnection.close()
