import requests as rq
import json
from pprint import pprint


def get_today_matches() -> json:
    arr = [2, 3, 4, 6]
    for num_lig in arr:
        req = rq.get(
            f'http://livescore-api.com/api-client/scores/live.json?key=qACKZM1CUVIaCa3g&secret'
            f'=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&competition_id={num_lig}')
        # print(json.loads(req.text))
        return json.loads(req.text)['data']['match']


def get_match_events(match_id: int) -> json:
    req = rq.get(f"http://livescore-api.com/api-client/scores/events.json"
                 f"?key=qACKZM1CUVIaCa3g&secret=GD8GLhMdizlJoGWOgyzfkASfwAq9Ltps&id={match_id}")
    return json.loads(req.text)


if __name__ == '__main__':
    today = get_today_matches()
    pprint(today)
    first_id = today[0]['id']
    print("ID:", first_id)
    print()
    pprint(get_match_events(first_id))
    # pprint(get_today())
