import requests
import xml.etree.ElementTree as ET # cos I can't get json working
import time
import sys

author_list = []
h_index = {}
# replace xxxx with the your api key
headers = {'X-ELS-APIKey': 'xxxxxxxxxxxx',
           'View' : 'METRICS'}
api_url_base = 'https://api.elsevier.com/content/author/author_id/'

def author_retrieval(authorid):
    
  api_url = f"{api_url_base}{authorid}?apikey={headers['X-ELS-APIKey']}&view={headers['View']}"
  response = requests.get(api_url) 
  
  if response.status_code == 200:
      return response.content.decode('utf-8')
  else:
      return response.status_code

# Our list of scopus author id's which
# we need because the api does not use orcid
with open('scopus.txt') as author_file:
  for author in author_file:
    author_list.append(author.strip())

# setup toolbar
toolbar_width = 10
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
  time.sleep(0.1) # do real work here


  for author in author_list:
    # https://dev.elsevier.com/api_key_settings.html
    # we are limited to 5k queries per week at a rate of 2 per second
    page = author_retrieval(author)

    if type(page) != 'int':          # No error codes allowed
      tree = ET.fromstring(page)
      h_index[author] = tree[1].text # contains h-index score

  # update the bar
  sys.stdout.write("-")
  sys.stdout.flush()

  with open('scopus_hindex.txt', 'w') as file:
    for key in h_index:
      file.write(f"{key}, {h_index[key]}\n")

# define h_index KPI
def hindex_distribution(filename):
  gt80, gt70, gt50, gt40, gt20 = 0, 0, 0, 0, 0
  with open(filename, 'a') as file:
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

hindex_distribution('scopus_hindex.txt')

sys.stdout.write("]\n") # this ends the progress bar
