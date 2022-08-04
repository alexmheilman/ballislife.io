import requests
import json, os


def get_data_from_url(url, params={}):
	response = requests.get(url, params=params)
	return json.loads(response.content)


def get_all_players(
	page = 0,
	per_page = 25,
	search = ''
):
	url = 'https://www.balldontlie.io/api/v1/players'
	
	params = {
		'page' : page,
		'per_page' : per_page,
		'search' : search
	}

	return get_data_from_url(url, params)

	
### USE THIS FOR A SPECIFIC PLAYER ###
def get_player_data(player_number):

	url = 'https://www.balldontlie.io/api/v1/players/' + str(player_number)
	
	return get_data_from_url(url)


### CAN USE THIS FOR ALL TEAMS ###
def get_all_teams(
	page = 0,
	per_page = 30
):
	url = 'https://www.balldontlie.io/api/v1/teams'

	params = {
		'page': page,
		'per_page' : per_page
	}
	return get_data_from_url(url, params)

	
### USE THIS FOR A SPECIFIC TEAM ###
def get_team_data(team_number):

	url = 'https://www.balldontlie.io/api/v1/teams/' + str(team_number)
	
	return get_data_from_url(url)


def get_all_games(
	page = 0,
	per_page = 25, 
	dates = [],
	seasons = [],
	team_ids = [],
	postseason = None,
	start_date = None,    # ENTER SPECIFIC DATE HERE TO FILTER 
	end_date = None		  # ENTER SPECIFIC DATE HERE TO FILTER
):
	url = 'https://www.balldontlie.io/api/v1/games'

	params = {
		'page': page,
		'per_page': per_page,
		'dates[]': dates,
		'seasons[]': seasons,
		'team_ids[]': team_ids,
		'start_date': start_date,
		'end_date': end_date
	}

	if postseason is not None:
		params['postseason'] = postseason
	if start_date is not None:
		params['start_date'] = start_date
	if end_date is not None:
		params['end_date'] = end_date

	
	return get_data_from_url(url, params)


### USE THIS FOR A SPECIFIC GAME ###
def get_game_data(game_id):

	url = 'https://www.balldontlie.io/api/v1/games/' + str(game_id)
	
	return get_data_from_url(url)


### USE THIS TO GET ALL STATS ###
def get_all_stats(
	page = 0,
	per_page = 25, 
	dates = [],
	seasons = [],
	player_ids = [],
	game_ids = [],
	postseason = None,
	start_date = None,    # ENTER SPECIFIC DATE HERE TO FILTER 
	end_date = None		  # ENTER SPECIFIC DATE HERE TO FILTER
):
	url = 'https://www.balldontlie.io/api/v1/stats'

	params = {
		'page': page,
		'per_page': per_page,
		'dates[]': dates,
		'seasons[]': seasons,
		'player_ids[]': player_ids,
		'game_ids[]': game_ids,
		'postseason': postseason,
		'start_date': start_date,
		'end_date': end_date
	}

	if postseason is not None:
		params['postseason'] = postseason
	if start_date is not None:
		params['start_date'] = start_date
	if end_date is not None:
		params['end_date'] = end_date

	
	return get_data_from_url(url, params)


### USE THIS FOR SEASON AVERAGES ###
def get_all_averages(
	season = '',
	player_ids = []
):
	
	url = 'https://www.balldontlie.io/api/v1/season_averages' 
	
	params = {
		'season': season,
		'player_ids[]': player_ids
	}

	return get_data_from_url(url, params)

