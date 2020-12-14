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


def get_match_events(match_id: int) -> dict:
    req = rq.get(f"http://livescore-api.com/api-client/scores/events.json"
                 f"?key={KEY}&secret={SECRET}&id="
                 f"{match_id}&sort=5")
    return dict(json.loads(req.text))


def get_last_event(match_id: int) -> dict:
    req = get_match_events(match_id)
    return dict(req['data']['event'][-1])


def get_summary(match_id: int) -> dict:
    req = rq.get(f'http://livescore-api.com/api-client/matches/stats.json?match_id={match_id}'
                 f'&key={KEY}&secret={SECRET}')
    return dict(json.loads(req.text)['data'])


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
    pprint(get_summary(first_id))
