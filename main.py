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

# PART C: Numbers as indices (loc vs iloc)

# Create a series with runtime as the index
runtime_lookup = pd.Series(df['title'].values, index=df['runtime'])
runtime_lookup = runtime_lookup.sort_index()
print(runtime_lookup)


# FIlter series by removing movies > 180 min
# and < 10 min, pulling only rows that are in between
condition2 = (runtime_lookup.index > 10) & (runtime_lookup.index < 180)
runtime_lookup = runtime_lookup[condition2]
print(runtime_lookup)


# Use our series look_up object to answer questions
# How many movies are exactly 40 minutes long?
print(runtime_lookup.loc[40].shape) # .loc retrieves by explictit index
# 42

print(runtime_lookup.iloc[100]) # what movie is at the 100th row here?
# the i in iloc stands for "implicit" like the implied inde rather then the index that's explicitly there