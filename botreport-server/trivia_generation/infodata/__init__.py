from typing import TypedDict
from datetime import date


def merge_from(source: dict, dest: dict, override=False):
    for key, value in source.items():
        if isinstance(value, dict):
            node = dest.setdefault(key, {})
            merge(value, node)
        else:
            '''
            if key in dest.keys():
                if override:
                    dest[key] = value
            '''
            dest[key] = value
    return dest
    

class InfoSource:
    def __init__(self):
        raise NotImplementedError

    def get_team(self, query: str):
        raise NotImplementedError

    def get_player(self, query: str):
        raise NotImplementedError

            
Player = {
    'name': None,

    'country_born': None,
    'country_play': None,

    'date_born': None,
    'height': None,
    'weight': None,

    'team': None
}
PlayerMask = {
    'name': 1.0,

    'country_born': 0.7,
    'country_play': 1.0,

    'date_born': 0.3,
    'height': 0.3,
    'weight': 0.3,

    'team': 1.0
}

Team = {
    'name': '',

    'country': '',
    
    'year_founded': 1970
}
TeamMask = {
    'name': 1.0,

    'country': 0.9,

    'year_founded': 0.5
}