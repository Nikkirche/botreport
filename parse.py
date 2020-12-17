import requests as rq
import json
from summery_to_text import summery_to_text
from pprint import pprint
from telegramm_write_bot import send_message_to_channel

KEY = "qACKZM1CUVIaCa3g"
SECRET = "GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps"
COMPETITIONS = [2, 3]


class Match:
    def __init__(self, match_id: int, data: dict):
        self.match_id = match_id
        self.counter_event = -1

        self.stats_home = {}
        self.stats_away = {}

        self.team_home = data['home_name']
        self.team_away = data['away_name']

        self.score_home = 0
        self.score_away = 0

        self.status = data['status']

        self.events = dict()

    def update(self):
        info = self._get_match_events()
        events = filter(lambda x: int(x['sort']) > self.counter_event, info['event'])
        list_of_events = list(events)
        for event in events:
            team = self.stats_home if event['home_away'] == 'h' else self.stats_away

            if event['player'] not in team:
                team[event['player']] = {}
                team[event['player']][event['event']] = 1
            else:
                if event['event'] not in team[event['player']]:
                    team[event['player']][event['event']] = 1
                else:
                    team[event['player']][event['event']] += 1
            if event['home_away'] == 'h':
                self.stats_home = team
            else:
                self.stats_away = team
        self.counter_event = len(info['event']) - 1

        self.score_home, self.score_away = map(int, info['match']['score'].split(' - '))
        self.status = info['match']['status']

        for event in list_of_events:
            event['score_home'] = self.score_home
            event['score_away'] = self.score_away
            event['team_home'] = self.team_home
            event['team_away'] = self.team_away

        self.events = list_of_events

    def _get_match_events(self) -> dict:
        req = rq.get(f"http://livescore-api.com/api-client/scores/events.json"
                     f"?key={KEY}&secret={SECRET}&id="
                     f"{self.match_id}&sort=5")
        return json.loads(req.text)['data']

    def get_summary(self) -> str:
        req = rq.get(f'http://livescore-api.com/api-client/matches/stats.json?match_id='
                     f'{self.match_id}'
                     f'&key={KEY}&secret={SECRET}')
        result = dict(json.loads(req.text)['data'])
        result['score_home'] = self.score_home
        result['score_away'] = self.score_away
        result['team_home'] = self.team_home
        result['team_away'] = self.team_away
        return summery_to_text(result)

    def get_player_stats(self, name: str) -> dict:
        return self.stats_home['h'][name] if name in self.stats_home['h'].keys() \
            else self.stats_away['a'][name]

    def get_status(self):
        return self.status

    def get_events(self):
        return self.events

    def count_penalty_home(self) -> int:
        return self.__count_penalty('h')

    def count_penalty_away(self) -> int:
        return self.__count_penalty('a')

    def __count_penalty(self, team) -> int:
        ans = 0
        stats = self.stats_home if team == 'h' else self.stats_away
        print(list(stats.values()))
        for stat in stats.values():
            if "GOAL_PENALTY" in stat:
                ans += stat['GOAL_PENALTY']
        return ans

    def __eq__(self, other):
        return self.match_id == other


class Controller:
    def __init__(self):
        self.matches = []
        self._generate_matches()

    def get_today_matches(self) -> dict:
        # arr = [2, 3, 4, 6, 45]
        competitions = COMPETITIONS
        ans_dict = dict()
        for competition in competitions:
            # req = rq.get(
            #     f'http://livescore-api.com/api-client/scores/live.json?key={KEY}&secret'
            #     f'={SECRET}&competition_id={competition}')
            req = rq.get(f'http://livescore-api.com/api-client/scores/history.json?key={KEY}'
                         f'&secret={SECRET}&from=2020-12-12&to=2020-12-13&competition_id=2')
            # print(json.loads(req.text))
            data = json.loads(req.text)
            for dat in data['data']['match'][:5]:
                ans_dict[dat['id']] = dat
            return ans_dict

    def _generate_matches(self):
        for id_match, data_of_match in self.get_today_matches().items():
            self.matches.append(Match(id_match, data_of_match))

    def update_all_matches(self):
        for match in self.matches:
            match.update()

    def add_new_matches(self):
        matches = self.get_today_matches()
        for id_match, data in matches.items():
            if id_match not in self.matches:
                self.matches.append(Match(id_match, data))

    def clear_matches(self):
        for index, match in enumerate(self.matches):
            if match.get_status() == 'FINISHED':
                send_message_to_channel("SUMMERY", match.get_summary())
                self.matches.pop(index)

    def get_all_matches(self):
        return self.matches

    def match_by_index(self, index: int):
        return self.matches[index]

    def __getitem__(self, index):
        return self.matches[index]

    def __len__(self):
        return len(self.matches)


if __name__ == '__main__':
    test = Controller()
    # test.update_all_matches()
    match = test[3]
    match.update()
    pprint(match.get_events())
    # test.clear_matches()
    # print(match.get_summary())

    # print(match.stats_home)

    # today = get_today_matches()
    # # pprint(today)
    # first_id = list(today.keys())[10]
    # first_data = list(today.values())[10]
    # pprint(first_id)
    # match = Match(first_id, first_data)
    # match.update()
    # pprint(match.stats_home)
    # print(match.score_home, match.stats_away, match.team_home)
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
asdasdasdasd
"""
