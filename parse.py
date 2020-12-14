import requests as rq
import json
from pprint import pprint

KEY = "qACKZM1CUVIaCa3g"
SECRET = "GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps"


def get_today_matches() -> dict:
    # arr = [2, 3, 4, 6, 45]
    arr = [45]
    ans_dict = dict()
    for num_lig in arr:
        # req = rq.get(
        #     f'http://livescore-api.com/api-client/scores/live.json?key={KEY}&secret'
        #     f'={SECRET}&competition_id={num_lig}')
        req = rq.get('http://livescore-api.com/api-client/scores/history.json?key=qACKZM1CUVIaCa3g'
                     '&secret=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&from=2020-12-12&to=2020-12-13')
        # print(json.loads(req.text))
        data = json.loads(req.text)
        for dat in data['data']['match']:
            ans_dict[dat['id']] = [dat['status'], dat['score'], dat['time']]
        return ans_dict


class Match:
    def __init__(self, match_id: int, data: dict):
        self.match_id = match_id
        self.counter_event = -1
        self.stats = {
            'h': {},  # home command
            'a': {}  # away command
        }
        self.teams_names = {
            'h': data['home_name'],
            'a': data['away_name']
        }
        self.score = {
            'h': 0,
            'a': 0
        }
        self.status = data['status']

    def update(self):
        info = self._get_match_events()
        events = filter(lambda x: x['sort'] > self.counter_event, info['event'])
        for el in events:
            self.stats[el['home_away']][el['player']][el['event']] += 1
        self.score['h'], self.score['a'] = map(int, info['match']['match_score'].split(' - '))

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
        return self.stats['h'][name] if name in self.stats['h'].keys() else self.stats['a'][name]


if __name__ == '__main__':
    today = get_today_matches()
    # pprint(today)
    first_id = list(today.keys())[0]

    # print("ID:", first_id)
    # print()
    # pprint(get_match_events(first_id))
    # print()
    # pprint(get_last_event(first_id))
    # pprint(get_today())
    # pprint(get_summary(first_id))
