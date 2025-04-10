# script to clean data sets and remove any unused columns.

import pandas as pd
file_name = "data/" + input("enter name of features file to be used: ")
with open(file_name, 'r') as f:
    columns_to_keep = [line.strip() for line in f if line.strip()]

#df = pd.read_csv('MLB_player_stats_[Insert Year].csv')
df = pd.read_csv("data/processed/combined_player_stats.csv")
#Remove PA > 40
df = df[df['PA'] > 40]

df = df[[col for col in columns_to_keep if col in df.columns]]

df.to_csv('data/processed/nicks_dataset.csv', index=False)
