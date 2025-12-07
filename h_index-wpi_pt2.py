import json
import yaml
import os
from lib import hindex

indexes = [] # store H-Index
impacts = [] # store impact facter

with open('config/reporting.yaml', 'r') as file:
    cf = yaml.safe_load(file)

directory_path = cf['openalex']['outpath']
contents = os.listdir(directory_path)
print(f"Contents of '{directory_path}':")
for item in contents:
	if not item.startswith('.') and item != "orcid_errors.txt" :
	# if not item.startswith('.') and item.startswith('F'):
		with open(os.path.join(directory_path, item), 'r') as file:
			author_oa = json.load(file)

		try:
			if isinstance(author_oa, dict):
				indexes.append(author_oa.get('results')[0]['summary_stats']['h_index'])
				impacts.append(author_oa.get('results')[0]['summary_stats']['2yr_mean_citedness'])
		except Exception as e:
			print(item)


print(hindex.hindex_distribution(indexes))
