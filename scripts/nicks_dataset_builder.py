import sys
print(sys.executable)
import os
print("Current working directory:", os.getcwd())
import json
import pandas as pd

# players on multiple teams that did not get any at bats for one of the teams will not get their weighted team factor
# be sure to drop when cleaning out files.

# Constants
SEASONS = range(2015, 2025)  # 2015-2024

# Debug Mode Variables
standard_count = 0
weighted_count = 0

# Initialize an empty DataFrames for appending info during loop
season_factor_df = pd.DataFrame(columns=['season', 'HR_total'])
combined_data_df = pd.DataFrame()
season_factor_dict = {}
# Loop through each season
for season in SEASONS:
    print(f"Processing season {season}...")

    # Load data files
    team_stats_file = f'data/raw/team_stats_{season}.csv'
    player_stats_file = f'data/raw/MLB_player_stats_{season}.csv'
    player_stats_split_file = f'data/raw/MLB_player_stats_{season}_with_team_split.csv'

    team_stats_df = pd.read_csv(team_stats_file)
    player_stats_df = pd.read_csv(player_stats_file)
    player_stats_team_split_df = pd.read_csv(player_stats_split_file)

    team_stats_df.insert(0, "tmFactor", 0)
    team_stats_df["tmFactor"] = team_stats_df["HR"]/max(team_stats_df["HR"])

    # Generate team factor dictionary (team name -> team factor)
    team_factor = team_stats_df.set_index("Team")["tmFactor"].to_dict()

    # Generate season factor dictionary (season -> season factor)
    season_factor_dict[season] = team_stats_df['HR'].sum()

    # Handle players who played for multiple teams (weighted team factors)
    # Filter players who played for multiple teams and calculate weighted team factor
    player_weighted_dict = {}
    for player_id in player_stats_team_split_df['MLBAMID'].unique():
        player_data = player_stats_team_split_df[player_stats_team_split_df['MLBAMID'] == player_id]
        
        # Skip single-team players
        if len(player_data['Team'].unique()) == 1:
            continue
        
        split_factor = 0.0
        total_pa = 0
        for _, row in player_data.iterrows():
            split_factor += (team_factor[row['Team']] * row['PA'])
            total_pa += row['PA']

        
        player_weighted_dict[player_id] = split_factor/total_pa
        weighted_count += 1

    # Standard team factor assignment (players who only played for one team)
    standard_count += len(player_stats_team_split_df) - len(player_weighted_dict)

    # Replace team names with team factors in player data this will skip players that played for more than one team, as "- - -" is not a key in this dictionary
    player_stats_df.insert(0,  "tmFactor", 0)
    
    # converting key into int and storing in json file for debugging
    player_weighted_dict_int_keys = {int(key): value for key, value in player_weighted_dict.items()}
    with open(f"weighted_team_factors_{season}.json", "w") as f:
        json.dump(player_weighted_dict_int_keys, f, indent=4)

    # applying team factors to players with multiple teams
    for index, row in player_stats_df.iterrows():
        if row['Team'] == '- - -':
            player_stats_df.at[index, 'tmFactor'] = player_weighted_dict.get(row['MLBAMID'])
        else:
            player_stats_df.at[index, 'tmFactor'] = team_factor.get(row['Team'])

    
    # Create a new row in a DataFrame format to store the total number of homeruns for the sesaon
    new_row = pd.DataFrame({'season': [season], 'HR_total': [team_stats_df['HR'].sum()]})

    # Concatenate the new row with the existing DataFrame to store season total homeruns
    season_factor_df = pd.concat([season_factor_df, new_row], ignore_index=True)

    # Combine data into the main dataset
    combined_data_df = pd.concat([combined_data_df, player_stats_df], ignore_index=True)

# generate dictionary of season factors
season_factor_df.insert(0, "season_factor", 0)
season_factor_df['season_factor'] = season_factor_df['HR_total']/max(season_factor_df['HR_total'])
season_factor_dict = season_factor_df.set_index('season')['season_factor'].to_dict()

# Add season factor to the dataframe
combined_data_df.insert(0, "season_factor", 0)
combined_data_df["season_factor"] = combined_data_df["Season"].map(season_factor_dict)

# scale players age, 50 chosen as no players over the age of 50, and seems like a safe number if new data was to be used for a futer prediction
combined_data_df['Age'] = combined_data_df['Age']/50

# Save combined dataset
combined_data_df.to_csv("data/processed/combined_player_stats.csv", index=False)

# Extract the column names from the dataframe
column_names = combined_data_df.columns.tolist()

# Write the column names to a text file
with open('../../data/full_feature_list.txt', 'w') as f:
    for column in column_names:
        f.write(column + '\n')


print(f"Finished processing. Total players with standard team factors: {standard_count}, weighted team factors: {weighted_count}")
