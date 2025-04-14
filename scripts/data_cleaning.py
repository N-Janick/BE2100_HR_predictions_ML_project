# script to clean data sets and remove any unused columns.

import pandas as pd
infile_name = "data/" + input("enter name of features file to be used: ") + ".txt"
outfile_name = "data/processed/" + input("enter file name for cleased dataset:  ") +  ".csv"
with open(infile_name, 'r') as f:
    columns_to_keep = [line.strip() for line in f if line.strip()]

# df = pd.read_csv('MLB_player_stats_[Insert Year].csv')
df = pd.read_csv("data/processed/combined_player_stats.csv")
# Remove PA > 40
plate_appearances = int(input("Enter minimum plate appearances "))
df = df[df['PA'] >= plate_appearances]

df = df[[col for col in columns_to_keep if col in df.columns]]

df.to_csv(outfile_name, index=False)
