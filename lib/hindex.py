import requests
import xml.etree.ElementTree as ET # cos I can't get json working
import time
import sys
import yaml

def get_data(config_file='config/reporting.yaml'):
	result      = {}
	author_list = []

	with open(config_file, 'r') as file:
		cf = yaml.safe_load(file)

	with open(cf['data']['saef_scopus']) as author_file:
		for author in author_file:
			author_list.append(author.strip())

	result['url']    = cf['openalex']['url']
	result['auth']   = author_list

	return result


def author_retrieval(orcid):
	time.sleep(1) # sleep for 1 second
	
	hdrs = get_data()

	api_url  = f"{hdrs.get('url')}{orcid}"
	response = requests.get(api_url) 
  
	if response.status_code == 200:
		return response.content.decode('utf-8')
	else:
		return response

def h_index(page, authorid):
  # page = author_retrieval(author)

  if type(page) != 'int':          # No error codes allowed
    tree = ET.fromstring(page)
    # tree[1].text # contains h-index score

  with open('scopus_hindex_2024.txt', 'a') as file:
  	file.write(f"{authorid}, {tree[1].text}\n")

# define h_index KPI
def hindex_distribution(filename):
  gt80, gt70, gt50, gt40, gt20 = 0, 0, 0, 0, 0
  with open(filename, 'r') as file:
    for line in file:
      score = int(line.split(',')[1])
      if score > 80:
        gt80 += 1
      if score > 70:
        gt70 += 1
      if score > 50:
        gt50 += 1
      if score > 40:
        gt40 += 1
      if score > 20:
        gt20 += 1
  return f">80: {gt80} >70: {gt70} >50: {gt50} >40: {gt40} >20: {gt20}"
