import requests as rq
import json
from pprint import pprint


def get_today_matches() -> json:
    # arr = [2, 3, 4, 6, 45]
    arr = [45]
    ans_dict = dict()
    for num_lig in arr:
        req = rq.get(
            f'http://livescore-api.com/api-client/scores/live.json?key=qACKZM1CUVIaCa3g&secret'
            f'=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&competition_id={num_lig}')
        # print(json.loads(req.text))
        data = json.loads(req.text)
        for dat in data['data']['match']:
            ans_dict[dat['id']] = [dat['status'], dat['score'], dat['time']]
        return json.dumps()


def get_match_events(match_id: int) -> json:
    req = rq.get(f"http://livescore-api.com/api-client/scores/events.json"
                 f"?key=qACKZM1CUVIaCa3g&secret=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&id="
                 f"{match_id}&sort=5")
    return json.loads(req.text)


def get_last_event(match_id: int) -> json:
    req = get_match_events(match_id)
    return req['data']['event'][-1]


def get_summary(match_id: int) -> json:
    req = rq.get(f'http://livescore-api.com/api-client/matches/stats.json?match_id={match_id}'
                 '&key=qACKZM1CUVIaCa3g&secret=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps')
    return json.loads(req)['data']


if __name__ == '__main__':
    today = get_today_matches()
    pprint(today)
    # first_id = today[0]['id']
    # print("ID:", first_id)
    # print()
    # pprint(get_match_events(first_id))
    # print()
    # pprint(get_last_event(first_id))
    # pprint(get_today())
