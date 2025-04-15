
import os
import pandas as pd

# Directory containing your CSV files
directory = os.getcwd()


# Create an empty list to hold dataframes
dfs = []

# Loop over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        # Read the CSV file into a DataFrame and append it to the list
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatenate all dataframes in the list into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('data/raw/MLB_player_stats_2015_2024.csv', index=False)
