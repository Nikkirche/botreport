import random

import parse


class Event():
    def __init__(self, data):
        self.id = data.get("id")
        self.match_id = data.get("match_id")
        self.player = data.get("player")
        self.time = data.get("time")
        self.type = data.get("event")
        self.id_in_match = data.get("sort")
        if data.get("home_away") == data.get("team_away"):
            self.active = data.get("team_home")
            self.passive = data.get("team_away")
            self.score_active = data.get("score_home")
            self.score_passive = data.get("score_away")
        else:
            self.active = data.get("team_away")
            self.passive = data.get("team_home")
            self.score_active = data.get("score_away")
            self.score_passive = data.get("score_home")


class TextGenerator():
    def generate(self):
        controller = parse.Controller()
        match = controller[0]
        match.update()
        events = match.get_events()
        print(events)
        patterns = [["test"], ["tesrt"], ["testr"], ["jg"], ["ghcf"], ["fuy"]]
        for i in events:
            event = Event(i)
            objects = dict(player=event.player, time=event.time, id_in_match=event.id_in_match,
                           active=event.active, passive=event.passive,
                           score_active=event.score_active, sore_passive=event.score_passive)
            if event.type == "YELLOW_CARD":
                i = random.randint(0, len(patterns[0]) - 1)
                text = patterns[0][i].format(objects)
            elif event.type == "YELLOW_RED_CARD":
                i = random.randint(0, len(patterns[1]) - 1)
                text = patterns[1][i].format()
            elif event.type == "RED_CARD":
                i = random.randint(0, len(patterns[2]) - 1)
                text = patterns[2][i].format()
            elif event.type == "GOAL":
                i = random.randint(0, len(patterns[3]) - 1)
                text = patterns[3][i].format(objects)
            elif event.type == "OWN_GOAL":
                i = random.randint(0, len(patterns[4]) - 1)
                text = patterns[4][i].format()
            elif event.type == "GOAL_PENALTY":
                i = random.randint(0, len(patterns[5]) - 1)
                text = patterns[5][i].format()
            return text


print(TextGenerator().generate())
