# CS 4042  Group Project

Data is sourced from: https://www.basketball-reference.com/leagues/

All data so far is for Regular Season games.

Potential tasks:

Create a pipeline where the user can input what data they want / what visualisations they want / how to export the data.

1. Cleaning data:

- Removed top row (extra indexes) of shooting stats
- Imported the data into dataframes in respected tables
- Removed all players with less than 5 games player
- Add team name to the player name, and 
- adjust rank accordingly
- Combine multiple years? Adjust rank?

2. Visualise data:

- Create a function to generate bar graphs based on inputted x value
- Create a function to generate scatterplot graphs based on iputted x and y values
- Histograms?
- Visualise specified players most common position as a half-court image with percentages (from shooting data)?
- Use basic KNN to identify most similar player to player specified in input

3. Create run loop:

- On run list options for user
- Allow user to select which functions to run on which data
- Run functions, if error list exception (use try:... except e:...)
- Allow exit loop by entering 0

4. Report:

- Make Google docs
- Introduce tasks
- Describe data
- Describe preprocessing
- Describe functions
- Add graphs
- Explain run / install guide (add ReadMe.md)