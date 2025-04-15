# Contact List update process

### FileMaker
People_Detail Layout

 - Execute "Contact List" search [Optional: Also defined in contact_list.sql]
 or
 - Export all

people_Projects Layout
 - Export all

### Python

python3 lib/cross_tab.py data/all/BIB_saef_20250401.json data/all/saef_library.db

### SQLITE

### On subsequent runs, empty the table
DROP TABLE ppl_projects;
DROP TABLE ppl;

### Recreate tables
.read GitHub/arcsaef/sql/creation.sql

## Import Filemaker People-Project export
### N.B. file for import needs to have UNIX line enedings.
.separator "\t" "\n"
.import GitHub/arcsaef/data/ppl_projects.tab ppl_projects
.import GitHub/arcsaef/data/people.tab ppl


### Create author key
UPDATE ppl SET author_key = first_name || last_name;

## Create a Contact List
.output GitHub/arcsaef/data/contact_list.csv
.read GitHub/arcsaef/sql/contact_list.sql
