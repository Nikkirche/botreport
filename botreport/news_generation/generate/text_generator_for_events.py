import random



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

    def format_text(self, patterns):
        objects = dict(player=self.player, time=self.time, id_in_match=self.id_in_match,
                       active=self.active, passive=self.passive,
                       score_active=self.score_active, score_passive=self.score_passive)
        if self.type == "YELLOW_CARD":
            i = random.randint(0, len(patterns["YELLOW_CARD"]) - 1)
            text = patterns["YELLOW_CARD"][i].format(**objects)
        elif self.type == "YELLOW_RED_CARD":
            i = random.randint(0, len(patterns["YELLOW_RED_CARD"]) - 1)
            text = patterns["YELLOW_RED_CARD"][i].format(**objects)
        elif self.type == "RED_CARD":
            i = random.randint(0, len(patterns["RED_CARD"]) - 1)
            text = patterns["RED_CARD"][i].format(**objects)
        elif self.type == "GOAL":
            i = random.randint(0, len(patterns["GOAL"]) - 1)
            text = patterns["GOAL"][i].format(**objects)
        elif self.type == "OWN_GOAL":
            i = random.randint(0, len(patterns["OWN_GOAL"]) - 1)
            text = patterns["OWN_GOAL"][i].format(**objects)
        elif self.type == "GOAL_PENALTY":
            i = random.randint(0, len(patterns["GOAL_PENALTY"]) - 1)
            text = patterns["GOAL_PENALTY"][i].format(**objects)
        return text


def read_patterns():
    file = open("patterns.txt")
    patterns = {"YELLOW_CARD": [], "YELLOW_RED_CARD": [], "RED_CARD": [], "GOAL": [], "OWN_GOAL": [],
                "GOAL_PENALTY": []}
    read_started = False
    for line in file:
        if not read_started and line == "start\n":
            read_started = True
        elif read_started and line[:6] == "type =":
            current = line[8:len(line) - 2]
        elif line == "exit":
            file.close()
            break
        elif line[0] == "#":
            pass
        else:
            patterns[current].append(line.rstrip())
    return patterns
