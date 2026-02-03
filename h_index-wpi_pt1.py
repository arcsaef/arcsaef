from lib import hindex
import json
import time
import yaml
import requests

# This script stores an open ales json file per resarcher
# Errors are researcher names without a json file
# USE the config file to adjust external variables e.g. directory location

hdrs = hindex.get_data()
with open('config/reporting.yaml', 'r') as file:
    cf = yaml.safe_load(file)

# A call is made to openalex per researcher in orcids.txt - the orcid file will be replaced with a function soon. NAH :)
oa_url  = hdrs.get('url')
indexes = [] # store H-Index
impacts = [] # store impact facter
errors  = cf['openalex']['errors']
    
for o in hdrs.get('orcids'):
    orcid    = o.split('|')[0]
    fullname = o.split('|')[2].replace(' ', '')
    filename = f"{cf['openalex']['outpath']}{fullname}.json"
    oa_api   = f"{oa_url}{orcid}"

    response = requests.get(f"{oa_api}")
    time.sleep(1) 
      
    if response.status_code == 200:
        page =  response.json() #json.loads(response.content) # dictionary 
        with open(filename, mode= "w", encoding="utf-8") as f:
            json.dump(page, f)
    else:
        with open(errors, mode= "a", encoding="utf-8") as f:
            f.write(fullname)
            f.write("\n")
