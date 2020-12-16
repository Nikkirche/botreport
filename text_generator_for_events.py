import random

import parse

events_with_generated_text = dict()
score_away = 0
score_home = 0


def get_type_of_event(event):
    event_type = event.get('event')
    from_which_side = random.random()
    if event_type == "GOAL":
        types = get_types_of_goal(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_goals(event, types[i], from_which_side)
    elif event_type == "YELLOW_RED_CARD":
        types = get_types_of_yellow_red_card(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_yellow__red_card(event, types[i], from_which_side)
    elif event_type == "RED_CARD":
        types = get_types_of_red_card(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_red_card(event, types[i], from_which_side)
    elif event_type == "YELLOW_CARD":
        types = get_types_of_yellow_card(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_yellow_card(event, types[i], from_which_side)
    elif event_type == "OWN_GOAL":
        types = get_types_of_own_goal(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_own_goal(event, types[i], from_which_side)
    elif event_type == "GOAL_PENALTY":
        types = get_types_of_penalty_goals(event)
        i = random.randint(0, len(types) - 1)
        return generate_text_for_penalty_goal(event, types[i], from_which_side)


def get_types_of_goal(event):
    types = []
    if (abs(score_away - score_home) > 2):
        types.append("DEFEATING")
    else:
        types.append("BASE1")
        types.append("BASE2")
        types.append("BASE3")
        types.append("BASE4")
    return types


def get_types_of_own_goal(event):
    types = ["test"]
    return types


def get_types_of_penalty_goals(event):
    types = ["test"]
    return types


def get_types_of_yellow_card(event):
    types = ["test"]
    return types


def get_types_of_yellow_red_card(event):
    types = ["test"]
    return types


def get_types_of_red_card(event):
    types = ["test"]
    return types


def generate_text_for_penalty_goal(event, types, from_which_side):
    return "test"


def generate_text_for_own_goal(event, types, from_which_side):
    return "test"


def generate_text_for_red_card(event, types, from_which_side):
    return "test"


def generate_text_for_yellow__red_card(event, types, from_which_side):
    return "test"


def generate_text_for_yellow_card(event, types, from_which_side):
    return "test"


def generate_text_for_goals(event, types, from_which_side):
    return "test"


dct = parse.Controller().get_today_matches()
f_id = list(dct.keys())[0]
dat = list(dct.values())[0]
match = parse.Match(f_id, dat)
match.update()
score_home = match.score_home
score_away = match.score_away
events = match.get_events()
print(events)
for i in events:
    print(get_type_of_event(i))
