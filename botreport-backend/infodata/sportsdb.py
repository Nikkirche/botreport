# from ..common import Player
from . import InfoSource
from datetime import datetime
import requests


class SportsDBInfoSource(InfoSource):
    def __init__(self, key=None):
        self.key = key
        self.url_players = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php'
        self.url_teams = 'https://www.thesportsdb.com/api/v1/json/1/searchteams.php'

    def get_team(self, query):
        params = {
            't': query
        }
        response = requests.get(self.url_teams, params=params)
        response = response.json()
        r = response['teams'][0]

        data = {
            'name': r.get('strTeam'),
            'country': r.get('strCountry'),

            'year_founded': r.get('intFormedYear'),

            'league_1': r.get('strLeague'),
            'league_2': r.get('strLeague2'),
            'league_3': r.get('strLeague3'),
            'league_4': r.get('strLeague4'),
        }
        return data

    def get_player(self, query):
        params = {
            'p': query
        }
        response = requests.get(self.url_players, params=params).json()
        r = response['player'][0]
        try:
            # Bad workaround for retired or deceased
            if r.get('strTeam').startswith('_'):
                Exception()
            team_data = self.get_team(r.get('strTeam'))
        except:
            team_data = {
                'name': None,
                'founded': None,
                'country': None
            }

        data = {
            'name': r.get('strPlayer'),

            'country_born': r.get('strNationality'),
            'country_play': team_data.get('country'),

            'date_born': r.get('dateBorn'),
            'height': r.get('strHeight'),
            'weight': r.get('strWeight'),

            'team': team_data.get('name'),
        }
        data = self.__cleanup(data)
        return data

    def __cleanup(self, data):
        if data['date_born'].startswith('0'):
            data['date_born'] = None
        return data