import requests as rq
import json
from pprint import pprint

KEY = "qACKZM1CUVIaCa3g"
SECRET = "GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps"


def get_today_matches() -> dict:
    # arr = [2, 3, 4, 6, 45]
    league = [45]
    ans_dict = dict()
    for num_lig in league:
        # req = rq.get(
        #     f'http://livescore-api.com/api-client/scores/live.json?key={KEY}&secret'
        #     f'={SECRET}&competition_id={num_lig}')
        req = rq.get(f'http://livescore-api.com/api-client/scores/history.json?key={KEY}'
                     f'&secret={SECRET}&from=2020-12-12&to=2020-12-13')
        # print(json.loads(req.text))
        data = json.loads(req.text)
        for dat in data['data']['match']:
            ans_dict[dat['id']] = dat
        return ans_dict


class Match:
    def __init__(self, match_id: int, data: dict):
        self.match_id = match_id
        self.counter_event = -1
        self.time = data['scheduled']

        self.stats_home = {}
        self.stats_away = {}

        self.team_home = data['home_name']
        self.team_away = data['away_name']

        self.score_home = 0
        self.score_away = 0

        self.status = data['status']

    def update(self):
        info = self._get_match_events()
        events = filter(lambda x: int(x['sort']) > self.counter_event, info['event'])
        for event in events:
            team = self.stats_home if event['home_away'] == 'h' else self.stats_away

            if event['player'] not in self.stats_home:
                team[event['player']] = {}
                team[event['player']][event['event']] = 1
            else:
                if event['event'] not in self.stats_home[event['player']]:
                    team[event['player']][event['event']] = 1
                else:
                    team[event['player']][event['event']] += 1
            if event['home_away'] == 'h':
                self.stats_home = team
            else:
                self.stats_away = team

        self.counter_event = len(info['event']) - 1
        self.score_home, self.stats_away = map(int, info['match']['score'].split(' - '))

    def _get_match_events(self) -> dict:
        req = rq.get(f"http://livescore-api.com/api-client/scores/events.json"
                     f"?key={KEY}&secret={SECRET}&id="
                     f"{self.match_id}&sort=5")
        return json.loads(req.text)['data']

    def get_summary(self) -> dict:
        req = rq.get(f'http://livescore-api.com/api-client/matches/stats.json?match_id='
                     f'{self.match_id}'
                     f'&key={KEY}&secret={SECRET}')
        return dict(json.loads(req.text)['data'])

    def get_player_stats(self, name: str) -> dict:
        return self.stats_home['h'][name] if name in self.stats_home['h'].keys() \
            else self.stats_away['a'][name]


if __name__ == '__main__':
    today = get_today_matches()
    # pprint(today)
    first_id = list(today.keys())[10]
    first_data = list(today.values())[10]
    pprint(first_id)
    match = Match(first_id, first_data)
    match.update()
    pprint(match.stats_home)
    print(match.score_home, match.stats_away, match.team_home, match.time)
    # print("ID:", first_id)
    # print()
    # pprint(get_match_events(first_id))
    # print()
    # pprint(get_last_event(first_id))
    # pprint(get_today())
    # pprint(get_summary(first_id))

"""
225275
{'ILGAZ SELIM': {'GOAL': 1},
 'PABLO': {'YELLOW_CARD': 1},
 'SALEM BOUPENDZA AARON': {'GOAL': 2}}
3 1 Hatayspor 10:30
"""
