import json
import yaml
import os
from lib import hindex

# This script
with open('config/reporting.yaml', 'r') as file:
    cf = yaml.safe_load(file)

indexes = [] # store H-Index
impacts = [] # store impact facter
directory_path = cf['openalex']['outpath']
contents 	   = os.listdir(directory_path)

with open(os.path.join(directory_path, 'score_triples.txt'), 'a') as outfile:

	for item in contents:
		if not item.startswith('.') and 'error' not in item:
			with open(os.path.join(directory_path, item), 'r') as file:
				author_oa = json.load(file)

			try:
				if isinstance(author_oa, dict):
					hindex  = author_oa.get('results')[0]['summary_stats']['h_index']
					imp_fct = author_oa.get('results')[0]['summary_stats']['2yr_mean_citedness']
					
					indexes.append(hindex)
					impacts.append(imp_fct)
					outfile.write(f"{item}, {hindex}, {imp_fct}, \n")
			except Exception as e:
				print(item)


try:
	print(hindex.hindex_distribution(indexes))
except Exception as e:
	print(e)
