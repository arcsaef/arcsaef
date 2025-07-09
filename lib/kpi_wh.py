import sqlite3
import sys
from sqlite3 import OperationalError

sqliteConnection = sqlite3.connect(sys.argv[1])
cursor_obj 		 = sqliteConnection.cursor()

def execute_script(filename):
    # Open and read the file as a single buffer
    with open(filename, 'r') as sql_file:
    	sql_script = sql_file.read()
    	result	   = cursor_obj.execute(sql_script)

    # return a list of tuples
    return result.fetchall()

x = execute_script('sql/contact_list.sql')
print(x)





cursor_obj.close()