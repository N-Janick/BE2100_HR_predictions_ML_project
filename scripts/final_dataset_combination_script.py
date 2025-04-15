import pandas as pd
import os

player_stats_fp = 'data/raw/MLB_player_stats_'
combined_dataset = pd.DataFrame()


# years to iterate over
for year in range(2015, 2025):
    print(f"Processing {year}...")

    # player data
    players = pd.read_csv(f"{player_stats_fp}{year}.csv")


    # append to combined dataset
    combined_dataset = pd.concat([combined_dataset, players], ignore_index=True)


# Final combined dataset is ready
print("All years processed. Final dataset shape:", combined_dataset.shape)

print(combined_dataset.head())

combined_dataset.to_csv('data/raw/MLB_player_stats_2015_2024.csv')
