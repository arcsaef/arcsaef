import argparse
import requests
import pickle
import yaml
import json
import os
from datetime import date
from datetime import datetime

''' '''
def get_url_filter(email, id, dte_1, dte_2):
    email = email # ADD YOUR EMAIL to use the polite pool
    # specify endpoint
    endpoint = 'works'
    # build the 'filter' parameter. 
    filters = f"institutions.ror:{id},from_publication_date:{dte_1},to_publication_date:{dte_2}"
    # put the URL together
    filtered_works_url = f'https://api.openalex.org/{endpoint}?filter={filters}'
    if email:
        return f"{filtered_works_url}&mailto={email}"

''' '''
def get_pages(email, org_url, dt1, dt2):
    # Credit: https://github.com/ourresearch/openalex-api-tutorials/blob/main/notebooks/getting-started/paging.ipynb
    page           = 1
    works          = []
    has_more_pages = True
    lt_10k_results = True
    filtered_url   = get_url_filter(email, org_url, dt1, dt2)

    # loop through pages
    while has_more_pages and lt_10k_results:

        # set page value and request page from OpenAlex
        url = f"{filtered_url}&page={page}"
        print('\n' + url)
        page_with_results = requests.get(url).json() 

        # loop through partial list of results
        results = page_with_results['results']
        
        for i, work in enumerate(results):
            openalex_id = work['id'].replace("https://openalex.org/", "")
            # if verbose:
            #   print(openalex_id, end='\t' if (i+1)%5!=0 else '\n') # Visual confirmation of download
            works.append(work)
        # next page
        page += 1

        # end loop when either there are no more results on the requested page 
        # or the next request would exceed 10,000 results
        per_page       = page_with_results['meta']['per_page']
        has_more_pages = len(results) == per_page
        lt_10k_results = per_page * page <= 10000
    return works

''' pickle OpenAlex pages '''
def pickle_page(filename, page):
  with open(filename, 'wb') as f:
    pickle.dump((page), f)

''' load up configuration file '''
def get_config(config_file='config/reporting.yaml'):      
    with open(config_file, 'r') as file:
        cf = yaml.safe_load(file)
    return cf

def main():
  # commandline options
  parser = argparse.ArgumentParser()
  parser.add_argument("-y", "--year", type=int, help="calendar year")

  args   = parser.parse_args()
  parser = argparse.ArgumentParser(description="Retrieve OpenAlex publication metadata",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-y", "--year", action="store_true", help="Temporal extent of data grab, default is current calendar year")
  parser.add_argument("-n", "--nbr", action="store_true",  help="Number of years, default is a single year")
  parser.add_argument("-v", "--verbose",  action="store_true", help="Print pages")

  date1=f"{date(date.today().year, 1, 1)}"
  date2=f"{date(date.today().year, 12, 31)}"

  if args.year:
    date1=f"{date(args.year, 1, 1)}"
    date2=f"{date(args.year, 12, 31)}"

  # load configuration file
  cf            = get_config() 
  email         = cf['openalex']['email']
  data_path     = f"{cf['openalex']['picklepath']}{datetime.strptime(date1, '%Y-%m-%d').year}"
  organisations = json.loads(cf['openalex']['organisations']) # load a dictionary

  print(f"Temporal extent: {date1} to {date2}")

  # download and pickle page
  for org_id, org_url in organisations.items():
    filename = f"{org_id.split('_')[0]}_works"
    org_page = get_pages(email, org_url, date1, date2)
    pickle_page(os.path.join(data_path, filename), org_page)

# roll
if __name__ == "__main__":
    main()
