import pandas as pd
import numpy as np
import sys


with open('data/all/crosstab_acp2025.csv', 'r') as f:
    crosstab_2025 = pd.read_csv(f)
with open('data/all/crosstab_acp2024.csv', 'r') as f:
    crosstab_2024 = pd.read_csv(f)
with open('data/all/crosstab_acp2023.csv', 'r') as f:
    crosstab_2023 = pd.read_csv(f)
with open('data/all/crosstab_acp2022.csv', 'r') as f:
    crosstab_2022 = pd.read_csv(f)
with open('data/all/crosstab_acp2021.csv', 'r') as f:
    crosstab_2021 = pd.read_csv(f)

# Harmonise column headers
headers = []

for x in crosstab_2021.columns:
    if x != 'title' and x != 'pub_yr':
        if x not in headers:
             headers.append(x)
for x in crosstab_2022.columns:
    if x != 'title' and x !=  'pub_yr':
        if x not in headers:
             headers.append(x)
for x in crosstab_2023.columns:
    if x != 'title' and x !=  'pub_yr':
        if x not in headers:
             headers.append(x)
for x in crosstab_2024.columns:
    if x != 'title' and x !=  'pub_yr':
        if x not in headers:
             headers.append(x)
for x in crosstab_2025.columns:
    if x != 'title' and x !=  'pub_yr':
        if x not in headers:
             headers.append(x)

# Create an all of crosstab header
sorted_headers = sorted(headers)

# Bulk each crosstab
for m in sorted_headers:
    if m not in crosstab_2021.columns:
        # Add a new column 'C'
        crosstab_2021[m] = [0] * len(crosstab_2021)
for m in sorted_headers:
    if m not in crosstab_2022.columns:
        crosstab_2022[m] = [0] * len(crosstab_2022)
for m in sorted_headers:
    if m not in crosstab_2023.columns:
        crosstab_2023[m] = [0] * len(crosstab_2023)
for m in sorted_headers:
    if m not in crosstab_2024.columns:
        crosstab_2024[m] = [0] * len(crosstab_2024)
for m in sorted_headers:
    if m not in crosstab_2025.columns:
        crosstab_2025[m] = [0] * len(crosstab_2025)

# Sorts columns by name in ascending order
crosstab_2021.sort_index(axis=1, inplace=True)
crosstab_2022.sort_index(axis=1, inplace=True)
crosstab_2023.sort_index(axis=1, inplace=True)
crosstab_2024.sort_index(axis=1, inplace=True)
crosstab_2025.sort_index(axis=1, inplace=True)

# Assert: True
if(len(crosstab_2021.columns)==len(crosstab_2022.columns)==len(crosstab_2023.columns)== \
    len(crosstab_2023.columns)==len(crosstab_2024.columns)==len(crosstab_2025.columns) ):
    res = pd.concat([crosstab_2021, crosstab_2022, crosstab_2023, crosstab_2024, crosstab_2025])
    column_title = res.pop('title')
    res.insert(0, 'title', column_title)
    column_pubyr= res.pop('pub_yr')
    res.insert(1, 'pub_yr', column_pubyr)

    # Set the index to start from 1
    res.index = range(1, len(res) + 1)
    res.to_csv(f'data/all/acp_matrix.csv', index_label='row_id')
    print(res.shape)
else:
    print('Column headers do not have the same length, matrix not possible')
