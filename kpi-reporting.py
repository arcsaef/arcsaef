import importlib
from lib import kpi


### A brief what's where and why
# - Reporting data is from 3 sources;
#   - Filemaker: api output (via Postman) is saved as text
#     - data/kpi_reporting_yyyymmdd.txt
#   - Zotero: api output for reporting year (via Postman) is saved as json
#     - data/saef_library_postman_yyyymmdd.json
#   - Bibiliography: Zotero bibligraphy output & manual update is saved a xlsx
#     - data/all/zot_biblio.xlsx
# - Updating config/reporting.yaml is __critical__


data           = kpi.load_data()
rpt_config     = kpi.get_rpt_args()
saef_library   = kpi.get_saef_library()
responses_json = kpi.split_response(data[0])
ppl_collection = kpi.person_construct(responses_json, rpt_config[0])
proj_saef      = kpi.project_construct(responses_json, ppl_collection[0])
# proj_saef      = kpi_wh.projects_construct(data[3])
# ppl_collection = kpi_wh.people_construct(data[3], rpt_config[0])
buckets        = kpi.matched_library(saef_library, ppl_collection[1])
templates      = kpi.load_templates()
meta_bucket    = buckets[0]
bucket         = buckets[1]
ppl_saef       = dict(sorted(ppl_collection[0].items(), key = lambda x: x[1].get('LastName')))
ppl_hash       = ppl_collection[1]
bulk_responses = data[0]
biblio         = data[1]
scopus         = data[2]
rpt_year       = rpt_config[0]
organisations  = rpt_config[1]
org_shortnames = list(organisations.keys())
proj_saef_nohold = proj_saef[proj_saef.Status != 'On hold']


# 1.remove empty rows
bucket = bucket[bucket['id_person'].isna() == False]
# 2. Make parsing more straight forward
for prsn in ppl_saef:
    if ppl_saef[prsn]['Gender'] == 'Non-binary/Gender diverse' or  ppl_saef[prsn]['Gender']  == 'Prefer not to say':
        ppl_saef[prsn]['Gender'] = 'Other'
# 3. Exclude: Nicole Webster, 027E2DEA-DB06-3946-B8C8-E053EF8E09F0
del ppl_saef['027E2DEA-DB06-3946-B8C8-E053EF8E09F0']; del ppl_hash['NicoleWebster']
# 4. Remove leading/trialing whitespace from  blibliographic entry.
biblio['Biblio'] = biblio['Biblio'].str.strip()
# 5. Jump into your pedantry
for prsn in ppl_saef:
    if ppl_saef[prsn]['Position'] != 'PhD Student' and  ppl_saef[prsn]['Position'] != 'Masters Student' and \
       ppl_saef[prsn]['Position'] != 'Honours Student':
        ppl_saef[prsn]['StudentProjectTitle'] = 'Not applicable'


# Organisation (annual & mid-year)
for org in org_shortnames:
    # Jasmine Lee 2025 workaround, B034D9D1-BA96-B640-8803-66889DCD5886
    if org == "QUT":
        ppl_saef['B034D9D1-BA96-B640-8803-66889DCD5886']['Org']          = "QUT"
        ppl_saef['B034D9D1-BA96-B640-8803-66889DCD5886']['Organisation'] = "Queensland University of Technology"
    else:
        ppl_saef['B034D9D1-BA96-B640-8803-66889DCD5886']['Org']          = "Monash"
        ppl_saef['B034D9D1-BA96-B640-8803-66889DCD5886']['Organisation'] = "Monash University"

    templates['doc_org'].render(kpi.get_context_org(org, organisations, ppl_saef, bucket, biblio, rpt_year, proj_saef_nohold)[0])
    templates['doc_org'].save(f"/VOLUMES/T7/Workspace/GitHub/arcsaef/output/{rpt_year}/annual/org/{org}.docx")


