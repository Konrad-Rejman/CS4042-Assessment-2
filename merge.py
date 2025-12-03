
# ------------------------- README -------------------------------
# The following is an attempt at merging the player names.
# A player may have more than one row as they may have played for more than one team in a season.
# I have dropped this as the datasets all contained varying columns, meaning I would have to make a massive ruleset
# with how to merge each column (sum, average, first value).
# The reason this is an unnecessary addition, is because it doesn't remove duplicates.
# It simply merges more than one input of a player.

def merge_player_stats(df):
    # Dictionary to store all players, where they are located in the table and their teams
    player_dictionary = {}

    # Loops through all players
    for index, player in df["Player"].items():

        # Locate columns
        team = df.loc[index, "Team"]
        pos = df.loc[index, "Pos"] # positions
        g = df.loc[index, "G"] # games

        # Player not in dictionary, add them
        if player not in player_dictionary:
            player_dictionary[player] = {
                "first_index": index, # For original index
                "indices": [index], # Contains all indices where tha same name exists

                # The following contain all values to be modified
                "teams": set(),
                "positions": set(),
            }

        # Otherwise append duplicate indices to key
        else:
            player_dictionary[player]["indices"].append(index)

        # Collect team name if it isn't missing
        if not pd.isna(team):
            player_dictionary[player]["teams"].add(team)
        
        # Collect position played if it isn't missing
        if not pd.isna(pos):
            player_dictionary[player]["positions"].add(pos)

    rows_to_drop = []

    # Takes all the information per player
    for player, info in player_dictionary.items():
        first_index = info["first_index"]
        indices = info["indices"]

        teams = info["teams"]
        positions = info["positions"]

        # Teams
        if teams:
            # Join all teams together
            merged_teams = " / ".join(sorted(teams))
            # Replace previous cell
            df.loc[first_index, "Team"] = merged_teams

        # positions
        if pos:
            # Join all positions together
            merged_positions = " / ".join(sorted(positions))
            # Replace previous cell
            df.loc[first_index, "Pos"] = merged_positions

        # all indices except the first are duplicates to drop
        for i in indices:
            if i != first_index:
                rows_to_drop.append(i)

    # Drop duplicate rows and reset index
    if rows_to_drop:
        df.drop(index=rows_to_drop, inplace=True)
        df.reset_index(drop=True, inplace=True)

    print(player_dictionary)