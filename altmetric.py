import time
import requests
import json

# replace xxxx with the your api & digest  keys
headers = {'key':       'xxxxx',
           'digest' :   'xxxxx',
           'scope' :    'all',
           'timeframe': '3m'
           }

# https://help.altmetric.com/support/solutions/articles/6000241371-using-the-explorer-api
# Exploring data for all research outputs from the full Altmetric database
# with ORCID 0000-0001-7616-0594 mentioned in the past three months
endpoint = 'https://www.altmetric.com/explorer/api/research_outputs/journals?'

def author_retrieval(orcid):
  # Endpoint + digest + filters + key
  api_url = f"{endpoint}digest={headers['digest']}&filter%5Borcid%5D={orcid}&filter%5Bscope%5D={headers['scope']}&filter%5Btimeframe%5D={headers['timeframe']}&key={headers['key']}"
  response = requests.get(api_url) 
  
  if response.status_code == 200:
      return response.json()
  else:
      return response.status_code

x = author_retrieval(orcid)

# If you intend to iterate ove a list of orcid's
# restrict to no more than 1 request a second
# time.sleep(5)

# Iterate over all metadata for an orcid
for n in range(0, len(x['data'])):
  print(x['data'][n]['meta'])
