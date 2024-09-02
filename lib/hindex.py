import requests
import time
import sys
import yaml
import json

''' Get hold of the openalex api and orcid, full name doubles '''
def get_data(config_file='config/reporting.yaml'):
	hdrs     	  = {}
	author_list = []

	with open(config_file, 'r') as file:
		cf = yaml.safe_load(file)

	with open(cf['data']['orcid']) as author_file:
		for author in author_file:
			author_list.append(author.strip())

	hdrs['url']    = cf['openalex']['url']
	hdrs['orcids'] = author_list

	return hdrs

''' Get author page '''
def author_page(url):

	response = requests.get(url) 
  
	if response.status_code == 200:
		return json.loads(response.content) # dictionary 
	else:
		return response.status_code 

''' Get an author h-index score'''
def hindex(author_page):

	# No error codes allowed
  if isinstance(author_page, dict):          
    return int(author_page.get('summary_stats')['h_index'])
  else:
  	return None

''' Get the number of articles with >= 2.5 impact factor '''
def impact_factor(author_page):
	count = 0

	# No error codes allowed
	if isinstance(author_page, dict):
		return int(author_page.get('summary_stats')['2yr_mean_citedness'])
	else:
 		return None

''' Define h-index KPI '''
def hindex_distribution(hindexes):
  gt80, gt70, gt50, gt40, gt20 = 0, 0, 0, 0, 0

  for hindex in hindexes:
    if hindex >= 80:
      gt80 += 1
    if hindex >= 70 and hindex < 80:
      gt70 += 1
    if hindex >= 50 and hindex < 70:
      gt50 += 1
      pass
    if hindex >= 40 and hindex < 50:
      gt40 += 1
      pass
    if hindex >= 20 and hindex < 40:
      gt20 += 1
  return f">80: {gt80} >70: {gt70} >50: {gt50} >40: {gt40} >20: {gt20}"

''' Define >2.5 impact factor qty '''
def impact_factor_gt25(impact_factors):
	count = 0
	for i in impact_factors:
		if i >= 2.5:
			count += 1
	return count
