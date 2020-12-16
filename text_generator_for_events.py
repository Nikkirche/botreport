import random

import parse


def get_match():
    controller = parse.Controller()
    match = controller[0]
    match.update()
    return match


active, passive = 0, 0
score_active, score_passive = 0, 0
events_with_generated_text = dict()
match = get_match()


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
    if abs(score_active - score_passive) > 2:
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


def get_active_and_passive_team(event):
    global active, passive
    global score_active, score_passive
    active, passive, score_active, score_passive = (
    match.team_home, match.team_away, int(match.score_home), int(match.score_away)) if event.get(
        "home_away") == match.team_away else (
    match.team_away, match.team_home, int(match.score_away), int(match.score_home))


def generate():
    events = match.get_events()
    print(events)
    for i in events:
        get_active_and_passive_team(i)
        print(get_type_of_event(i))


generate()
# For adding new template - add in generate_event_type function
# if(*some case*):
#   types.append(*name of this case*)
# and in generate_text_event_type add
#    if game_type == *name of this case*:
#       if from_which_side:
#           return your template for active
#       else:
#           return your template for passive
# You can use events.get("player") for player name
# events.get("time") for events time
#  active,passive for team names(active is the intiator of event, passive the other one)
# score_active and score_passive to get score of active and passive team
