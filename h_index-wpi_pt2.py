import json
import yaml
import os
from lib import hindex

# This script uses the json files from _pt1
# to calucalte h-index spread and 
# USE the config file to adjust external variables e.g. directory location

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

				try:
					author_oa = json.load(file)

				except Exception as e:
					print(file)


			try:
				if isinstance(author_oa, dict):
					hindex  = author_oa.get('results')[0]['summary_stats']['h_index']
					imp_fct = author_oa.get('results')[0]['summary_stats']['2yr_mean_citedness']
					orcid   = author_oa.get('results')[0]['orcid']

					indexes.append(hindex)
					impacts.append(imp_fct)
					outfile.write(f"{orcid}, {item}, {hindex}, {imp_fct}, \n")
			except Exception as e:
				print(item)

# Use the spreadsheet to calculate because it is more transarent
# try:
# 	# H-index distributions (Scopus) (Researchers) >80:>70:>50:>40:>20
# 	print(hindex.hindex_distribution(indexes))
# except Exception as e:
# 	print(e)
