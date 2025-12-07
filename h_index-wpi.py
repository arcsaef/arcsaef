from lib import hindex
import json
import time
import yaml
import requests


hdrs = hindex.get_data()
with open('config/reporting.yaml', 'r') as file:
    cf = yaml.safe_load(file)

# A call is made to openalex per researcher in orcids.txt - the orcid file will be replaced with a function soon. NAH :)
oa_url  = hdrs.get('url')
indexes = [] # store H-Index
impacts = [] # store impact facter
errors  = cf['openalex']['errorpath']
    
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

print(hindex.hindex_distribution(indexes))

    # page     = hindex.author_page(f"{oa_api}")
    # hindex   = hindex.hindex(page)
    # impact   = hindex.impact_factor(page)

    # if isinstance(hindex, int):
    #     indexes.append(hdex)
    #     impacts.append(impact)

    #     with open(filename, mode= "w", encoding="utf-8") as f:
    #         json.dump(page, f)
    # else:
        # with open(errors, mode= "a", encoding="utf-8") as f:
        #     f.write(fullname)
        #     f.write("\n")
    #         time.sleep(1) # sleep for 1 second satisfies max 10 call per sec limit

# H-index distributions (Scopus) (Researchers) >80:>70:>50:>40:>20
# print(hindex.hindex_distribution(indexes))