

# lists of 
# player stats file name example '../../data/raw/MLB_player_stats_2015.csv' 
# player stats with team splits file name example '../../data/raw/MLB_player_stats_2015_with_team_splits.csv
# team stats file name example '../../data/raw/team_stats_2015.csv'

# filepath variables
# player_stats = '../../data/raw/MLB_player_stats_'
# team_stats = '../../data/raw/team_stats_'


# iterate through years of stats (2015 - 2024) for each year of data
# begin loop

#     load each stat category into a dataframe 
#     players = pd.read_csv(player_stats + str(<current year>) + '.csv')
#     players_with_splits = pd.read_csv(player_stats + str(<current year>) + '_with_team_splits.csv')
#     teams = ...

#     use team stats file to generate a dictionary of team names : team factor;
#     '''
#     # this snippet is how I worked out generating team factors per season and added them to players statlines.
#     # Loading the data set into a dataframe 
#     team_stats = pd.read_csv("../../data/raw/team_stats_2015.csv")

#     # adding a column for team factor feature
#     team_stats.insert(0, "tmFactor", 0)

#     # populating the team factor column for each team   
#     for _ in team_stats:
#         team_stats["tmFactor"] = team_stats["HR"]/max(team_stats["HR"])

#     # creating a dictionary of Team: team Factor
#     team_factor = team_stats.set_index("Team")["tmFactor"].to_dict()

#     # loading a season dataset and cleaning out some columns that are duplicates or
#     # appear to be blank on many rows based on a quick scan in excel
#     players =  pd.read_csv("../../data/raw/MLB_player_stats_2015.csv")
#     players = players[players['PA'] >= 20]
#     players = players.drop(columns=['Name.1', 'Team.1','UBR', 'wGDP', 'XBR'], axis=1)

#     # adding and populating team factor column on player stats data set
#     players.insert(0,  "tmFactor", 0)
#     players["tmFactor"] = players["Team"].map(team_factor)
#     '''

#     also sum up the home runs for the season and append to a season: season factor dictionary; see above snippet for examples of loading into a dictionary

#     teamsplits file drop each row with a unique playerID (this should leave me with just the players that played for multiple tems in a season;
#     use team factor dictionary to replace team name column with team factor;
#     calculate weighted team factors for these multiteam players and store in playerID : weighted team factor dictionary;

#     Iterate through the playerstats data (which includes the total stats for multipteam players, the team name is listed as '---') and replace team names with team factors from the generated dictionary
#     if team = '---' 
#         this will be replaced with weighted team factor based on correspnding playerID in the other generated dictionary;

#     append data to combined dataset dataframe;
# end of loop.

# There should be one large dataset that inlcudes all statlines, add a column for season Factor and populate it with the season factor that correspnds with that rows value for the season column.


