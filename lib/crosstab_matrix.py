import pandas as pd
import sys

# usage: python3 lib/crosstab_matrix.py data/all/data_acp2025.csv
fn = sys.argv[1]
with open(fn, 'r') as f:
    df = pd.read_csv(f, sep='|', names=['position', 'author_key', 'pub_yr', 'title'])

sorted_df = df.sort_values(by='author_key')

# crosstab the DataFrame÷
crosstab_df  = pd.crosstab(sorted_df['title'], sorted_df['author_key'])

# Insert 'pub_yr' at index 0 (first position). Slice data/all/crosstab_acp2025.csv
crosstab_df.insert(0, 'pub_yr', [fn[ -8: -4]] * len(crosstab_df) )

# print(crosstab_df)
crosstab_df.to_csv(f'data/all/crosstab_acp{fn[ -8: -4]}.csv')