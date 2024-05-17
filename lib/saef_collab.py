import os



''' '''
def saef_orcid(filepath):
    # SAEF researcher id triples: scopus id - orcid - name
    with open(filepath, 'r') as f:
        scopus_str = f.read()
    scopus_data = scopus_str.split('\n')

    return scopus_data

'''  '''
def get_collaboration(org_data, saef_data):
    # match saef orcids
    titles = {}
    orcids = []
    for line in scopus_data:
        ln = line.strip().split(',')
        if len(ln) > 1:
            orcids.append(ln[1])
    # loop through each page
    for page in org_data:
        title = page['title']
        for author in page['authorships']:
            if author['author']['orcid'] is not None:
                orcid = author['author']['orcid'].split('/')[-1]
                matched_auth = []
                if orcid in orcids:
                    matched_auth.append(f"{orcid} ; {saef_data[orcids.index(orcid)].split(',')[2]}")
        
            if len(matched_auth) > 0:
                titles[title] = matched_auth
    return titles

''' '''
def retrieval(filepath):
    for file in os.scandir("."):
        if file.is_file():
            print()
            with open(file, 'rb') as f:
                data = pickle.load(f)
                print(get_collaboration(data, scopus_data))
