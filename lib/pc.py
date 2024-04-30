import yaml
from collections import defaultdict, Counter

''' load project collaboration data '''
def load_data(data='data/all/project_collaborations.yaml'):
    with open(data, 'r') as file:
        pc = yaml.safe_load(file)
    return pc

def list_project_collab(project_collaboration):
  # list projects by most collaborated
  pc_list_a = []
  pc_list_b = []
  for i in project_collaboration['Projects']:
      if project_collaboration['Projects'][i]['internal'] is not None:
        pc_list_a.append(i)

  for i in pc_list_a:
    for e in project_collaboration['Projects'][i]['internal'].split(','):
      pc_list_b.append(e.strip())

  pc_list_b.sort()
  return Counter(pc_list_b).most_common()
  
def list_project_wo_collab(project_collaboration):
  # projects w/o listed internal collabrations
  for i in pc['Projects']:
      if pc['Projects'][i]['internal'] is None:
          print(f"{i}")
