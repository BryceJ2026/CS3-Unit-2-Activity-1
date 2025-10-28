import pandas as pd
import numpy as np


df = pd.read_csv('movies_metadata_v2.csv', encoding=' iso-8859-1').dropna(axis=1, how='all')
df.head()
df.shape
df.info()
print(df.head())
# Fill in brackets with a CONDITIONAL
budget_df = df[df['budget'] > 1000000]
print(budget_df.shape) #5
# Fill in the parameters for (values, index)
budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup)
print(budget_lookup['Jumanji']) #65 Mil

# First define the condition to be checked
condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index <= 'Byzantium')
# Pull rows conditionally
budget_lookup_A_B = budget_lookup[condition]

