# Contact List update process

### FileMaker
People_Detail Layout

 - Execute "Contact List" search [Optional: Also defined in contact_list.sql]
 or
 - Export all

people_Projects Layout
 - Export all

Assuming scripts are run from /Workspace prefix paths with Github/arcsaef/

### Python
#### # Crosstab: AI, CI PI, publication count over the years
python3 lib/cross_tab.py data/all/BIB_saef_20250401.json data/all/saef_library.db

### SQLITE
sqlite3 data/all/saef_library.db

### On subsequent runs, empty the table
DROP TABLE ppl_projects;
DROP TABLE ppl;

### Recreate tables
.read sql/creation.sql

## Import Filemaker People-Project export
### N.B. file for import needs to have UNIX line enedings.
.separator "\t" "\n"
#### Make sure the files have Unix line endings
.import data/ppl_projects.tab ppl_projects
.import data/people.tab ppl

### Create author key
UPDATE ppl SET author_key = first_name || last_name;

## Create a Contact List
.output data/contact_list.csv
.read   sql/contact_list.sql

## Update SAEF Member contact list
N.B. Do not open data/contact_list.csv in Excel! Use SublimeText :)
