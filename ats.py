import json

fp = "ats_dates_and_decisions.json"

with open(fp, 'r') as f:
  ats = json.load(f)

# E.g. usage: get_measures('can', 'measures_adopted_2000_onwards')
def get_measures(iso_country, measure):
  iso_country = iso_country.upper()
  for x in ats[iso_country][measure]:
    for k, v in x.items():
      print(f"{k}: {v}")
