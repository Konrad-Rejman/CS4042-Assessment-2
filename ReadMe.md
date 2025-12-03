# CS 4042  Group Project

Data is sourced from: https://www.basketball-reference.com/

All data so far is for Regular Season games.

Potential tasks:

Create a pipeline where the user can input what data they want / what visualisations they want / how to export the data.

1. Cleaning data:

- Some of the data has duplicates of player, because they player for multiple teams, can this data be combined?
- Some categories might not be as useful
- Allow sorting/filtering data by: MVP's only (and other awards), top 100 player, certain teams, conferences (East or West coast), position

2. Visualise data:

- Allow graphs of statistics (scatterpoint graphs) with a specified x and y axis
- Visualise specified players most common position as a half-court image with percentages (from shooting data)
- Use basic ML Model to identify most similar player in the data (does not have to be very accurate)

3. Export data as task specific CSV's

----------------------------------

## Oliwier - Pipeline rundown:

Preprocessing stayed the same like Konrad left it.

All of the code cells are commented, if you think it is unclear please let me know and I will simplify it further if I can

# Fixing tables:

Headings are merged in the case of two headers are present (only present on the shooting stats table, but it is made in a way to work on all if necessary)

Once Headings are merged, the other one is dopped to ensure only one heading.

Ensure columns have correct datatypes:
*String objects* for names, teams, etc.
*Floats* for integers like games played, decimals for percentages, etc.

Drops final column as it is reduntant player code info.
Drops final row as it just contains averages and missing values.

# Cleaning data:

Checks for duplicate rows and removes them. There is another version in the comments, we can change it if we want to.

Strips whitepsace from strings

Converts empty cells and common placeholders to NaN

Removes players that played less than 5 games - stastically insignificant

# Optional

I placed the start of my code for merging player names and its explanation in *merge.py*
As some players have played in more than one team, they have more than one row.
That is where the idea of merging player rows came from. ^^^
