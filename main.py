from datetime import date

import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_int64_dtype

df = pd.read_csv('./datas/Airbnb_NYC_2019.csv')
print('shape', df.shape)
missing_values_count = df.isnull().sum()
print('Missing values :-')
print(missing_values_count)

total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing / total_cells) * 100
print('percent_missing', percent_missing, '%')

# df = df.dropna(subset=['name', 'host_name'])
print("Total data size :- ", df.shape[0])

unique_ids = df['id'].unique()
print("Unique id size :- ", len(unique_ids))

unique_host_ids = df['host_id'].unique()
print("Unique host id size :- ", len(unique_host_ids))

# df = df.fillna(value={'host_name': 'None'})
# missing_values_count = df.isnull().sum()
# print('Missing values :-')
# print(missing_values_count)

# Code to enter the empty host_names using host_id's
# for i in range(df.shape[0]):
#     if pd.isna(df.at[i, 'host_name']):
#         host_id = df.at[i, 'host_id']
#         print(host_id)
#         for j in range(df.shape[0]):
#             if df.at[j, 'host_id'] == host_id and pd.notna(df.at[j, 'host_name']):
#                 df.at[i, 'host_name'] = df.at[j, 'host_name']

# Dropping data's with empty host_id's and host_name's
df = df.dropna(subset=['name', 'host_name'])
present_total_cells = np.product(df.shape)
percent_missing = 100 - ((present_total_cells / total_cells) * 100)
print('data dropped after clearing empty name and host_names', percent_missing, '%')

missing_values_count = df.isnull().sum()
print('Missing values :-')
print(missing_values_count)

# Percentage of hosts with 0 sale
print("Percentage of hosts with 0 sale :- ", missing_values_count['last_review'] / df.shape[0] * 100, "%")

# Setting the values of last_review and reviews_per_month
today = date.today()
values = {'reviews_per_month': 0, 'last_review': today}
df = df.fillna(value=values)

missing_values_count = df.isnull().sum()
print('Missing values :-')
print(missing_values_count)

df.to_csv('./results/clean_data.csv')

# Migrating data shifts from right to left by 1

# print('id dtype', df['id'].dtype)
# print('name dtype', df['name'].dtype)
# print('host_id dtype', df['host_id'].dtype)

# df.loc['id'] = pd.to_numeric(df.loc['id'], downcast='integer')
# df.loc['host_id'] = pd.to_numeric(df.loc['host_id'], downcast='integer')



# count = 0
# error_count = 0
# for i in range(df.shape[0]):
#     try:
#         if not is_int64_dtype(df.at[i, 'host_id']):
#             count += 1
#     except:
#         print(i)
#         error_count += 1
#         continue
# print(count, error_count)
#
# print(df.at[360, 'host_id'])



