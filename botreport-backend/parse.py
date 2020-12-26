import requests as rq
import json
from summary_to_text import summary_to_text
from pprint import pprint
from out_tg import send_message_to_channel
from out_db import new, post
from generator_events import *
from time import sleep
import infodata
from random import random, choice
from infodata import InfoSource, sportsdb
from generator_trivia import *
from translator import translate

KEY = "qACKZM1CUVIaCa3g"
SECRET = "GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps"
COMPETITIONS = [1, 2, 3, 4]


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

        self.events_patterns = read_patterns()

    def update(self, generator):
        prev_status = self.status
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
        if info['match']['score'] != '? - ?':
            self.score_home, self.score_away = map(int, info['match']['score'].split(' - '))
        self.status = info['match']['status']
        if self.status == 'IN PLAY' and prev_status == 'NOT STARTED':
            print("MATCH STARTED", self.team_home, self.team_away)
            send_message_to_channel('', f"Матч между {self.team_home} и {self.team_away} начался")

        for event in list_of_events:
            event['score_home'] = self.score_home
            event['score_away'] = self.score_away
            event['team_home'] = f"{self.team_home}"
            event['team_away'] = f"{self.team_away}"
            event['player'] = f"{event['player']}"

            cls_event = Event(event)
            text_event = cls_event.format_text(self.events_patterns)
            text_fact = generator.trivia_event(event)
            print(text_event + ' \n\n' + text_fact)
            translated_event = translate(text_event)
            translated_fact = translate(text_fact)
            result_text = translated_event + '\n\n' + translated_fact
            print(result_text)
            send_message_to_channel(event['event'], result_text)
            post(translated_event.replace('*', '').split('\n')[1], translated_fact, ' '.join([i.lower().capitalize() for i in event['player'].split()]), f'{self.team_home} VS {self.team_away}', info['match']['competition']['name'], event['event'])
        print(self.events)
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
        result['team_home'] = f"{self.team_home}"
        result['team_away'] = f"{self.team_away}"

        return translate(summery_to_text(result))

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

        sapi = sportsdb.SportsDBInfoSource()

        aggregator = InfoAggregator([sapi])
        self.generator = TriviaGenerator(aggregator, DEFAULT_TEAM, DEFAULT_PLAYER)

    def get_today_matches(self) -> dict:
        competitions = COMPETITIONS
        ans_dict = dict()
        for competition in competitions:
            '''req = rq.get(
                f'http://livescore-api.com/api-client/scores/live.json?key={KEY}&secret'
                f'={SECRET}&competition_id={competition}')'''
            req = rq.get(
                'http://livescore-api.com/api-client/scores/history.json?key=qACKZM1CUVIaCa3g&secret=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&from=2020-12-12&to=2020-12-14&&competition_id=2')

            # req = rq.get(f'http://livescore-api.com/api-client/scores/history.json?key={KEY}'
            #              f'&secret={SECRET}&from=2020-12-12&to=2020-12-13&competition_id=2')
            # print(json.loads(req.text))
            data = json.loads(req.text)
            # if not data['success']:
            #     print("Something went wrong")
            #     return {}
            for dat in data['data']['match']:
                ans_dict[dat['id']] = dat
        print(ans_dict)
        print("KEYS COUNTER:", len(ans_dict.keys()))
        return ans_dict

    def _generate_matches(self):
        for id_match, data_of_match in self.get_today_matches().items():
            self.matches.append(Match(id_match, data_of_match))

    def update_all_matches(self):
        for match in self.matches:
            match.update(self.generator)

    def add_new_matches(self):
        matches = self.get_today_matches()
        for id_match, data in matches.items():
            if data['status'] != 'FINISHED':
                print("From add new match function: Match finished")
                continue
            if id_match not in self.matches:
                self.matches.append(Match(id_match, data))

    def clear_matches(self):
        for index, match in enumerate(self.matches):
            if match.get_status() == 'FINISHED':
                pprint(match.get_summary())
                send_message_to_channel("summary", match.get_summary())
                self.matches.pop(index)

    def get_all_matches(self):
        return self.matches

    def match_by_index(self, index: int):
        return self.matches[index]

    def __getitem__(self, index):
        return self.matches[index]

    def __len__(self):
        return len(self.matches)


def test_load():
    controller = Controller()
    try:
        new()
    except Exception as e:
        print('Database already exists')
    while True:
        try:
            print(len(controller))
            controller.clear_matches()
            controller.add_new_matches()
            controller.update_all_matches()
        except KeyboardInterrupt:
            exit()
        except BaseException as ex:
            print(ex)
        print('iteration')
        sleep(120)


if __name__ == '__main__':
    test_load()
    # pass
    # test = Controller()
    # test.update_all_matches()
    # match = test[1]
    # match.update()
    # pprint(match.get_events())
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
