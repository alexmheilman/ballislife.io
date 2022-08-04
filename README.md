# Project Name (Comprehensive Basketball Stats)

This project can be used to find comprehensive, descriptive statistics from individual players, games, teams, and season stats

## Functions

The funcitons in this project wrap api endpoints from https://www.balldontlie.io. All you need to do is input the values for your favorite teams or players and the stats will be compiled in a .json file for you.

### Get All Players
	Use this function to pull stats for all players. 
	Parameters: 
	- This function requires no parameters. You can run the function as is and all the data will be pulled

### Get Specific Player
	This function will pull stats for a specific player. 
	 Parameters: 
	  - A number needs to be put into the brackets() of the data line to call a specific player

### Get All Teams 
	This function will pull stats for all NBA teams. 
	 Parameters:
	  - No parameters are needed. Will run as is. 

### Get Specific Team
	This function will pull stats for a specific team. 
	Parameters: 
	 - A number needs to be put in the brackets() of the data line to call a specific team. 

### Get All Games 
	This function can be used to get data on all games of an NBA season.
	Parameters:
	 - A start and end date can be entered on line 104 and 105 to look at a specific part of the season, but doesn't need to be. 
	 - Date format must be 'YYYY-MM-DD'

### Get Specific Game
	This function will pull the data for a specific game. 
	Parameters: 
	 - A number needs to be entered in the brackets() of the data line to access a specific game.


### Get All Stats
	This function can be used to pull all the stats for a season. 
	Parameters:
	 - start and end date can be entered to filter results to a specific part of the season, but doesn't need to be added
	 - Date format must be 'YYYY-MM-DD'

### Get All Averages
	This function can be used to get player averages from a season. 
	Parameters:
	 - season and player id must be entered to access a players stats. 
	 - Season is a string year 'YYYY'
	 - Player id is a string number '___'
	

### References

- Big shout out to the balldontlie API for providing all the data used.
- Please visit their site at 'balldontlie.io'
