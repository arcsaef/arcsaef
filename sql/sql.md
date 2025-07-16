# Contact List update process

### FileMaker
Main Layout

 - Execute DataExport script
 - All exported fields are saved to /Workspace/GitHub/arcsaef/data

Assuming scripts are run from /Workspace prefix paths with Github/arcsaef/

### SQLITE
sqlite3 data/all/saef_library.db

### Recreate tables
.read sql/creation.sql

## Import Filemaker People-Project export
### N.B. file for import needs to have UNIX line enedings.
.separator "\t" "\n"

#### Make sure the files have Unix line endings
.import data/kpi_ppl.tab ppl
.import data/kpi_projects.tab projects
.import data/kpi_organisations.tab organisations
.import data/kpi_grants.tab grants
.import data/kpi_workshops.tab workshops
.import data/kpi_prizes.tab prizes
.import data/kpi_ppl_advisory.tab ppl_advisory
.import data/kpi_ppl_grants.tab ppl_grants
.import data/kpi_ppl_workshops.tab ppl_workshops
.import data/kpi_ppl_supervision.tab ppl_supervision
.import data/tmp_ppl_projects.tab tmp_ppl_projects

### Populate ppl_projects, ppl
.read sql/populate.sql

## Create a Contact List
.output data/contact_list.csv
.read   sql/contact_list.sql

## Update SAEF Member contact list
N.B. Do not open data/contact_list.csv in Excel! Use SublimeText :)

### Python
#### # Crosstab: AI, CI PI, publication count over the years
python3 lib/cross_tab.py data/all/BIB_saef_20250401.json data/all/saef_library.db

