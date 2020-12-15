import random


# Info about the winner
def get_types_of_game(goals_1, goals_2):
    types = []
    if goals_1 < goals_2:
        goals_1, goals_2 = goals_2, goals_1
    if goals_1 == goals_2:
        print()
    elif (goals_1 - goals_2) > 0:
        if goals_2 == 0:
            types.append("unanswered")
        if (goals_1 - goals_2) > 2:
            types.append("smashing")
    return types


def generate_text_for_wins(game_type, winner, loser):
    # 0 for loser ,1 for winner
    from_which_side = random.random()
    if game_type == "unanswered":
        if from_which_side:
            return f"{winner} scored five unanswered goals in the gate {loser}"
        else:
            return f"Five unanswered goals scored to {loser}"

    elif game_type == "smashed":
        if from_which_side:
            return f"the {winner} defeated the {loser}"
        else:
            return f" {loser} was defeated"


def generate_text_for_drafts(game_type):
    from_which_side = random.random()


def find_loser_and_winner(goals_team_1, goals_team_2, team_1, team_2):
    if goals_team_2 > goals_team_1:
        winner = team_2
        loser = team_1
    else:
        winner = team_2
        loser = team_1
    return winner, loser


def is_draw(goals_1, goals_2):
    return goals_1 == goals_2


def main():
    # Sample Data
    score = "1:0"
    team_1 = "barnaul"
    team_2 = "barcelona"
    goals_team_1 = int(score[0])
    goals_team_2 = int(score[2])
    types = get_types_of_game(goals_team_1, goals_team_2)
    i = random.randint(0, len(types) - 1)
    if not is_draw(goals_team_1, goals_team_2):
        roles = find_loser_and_winner(goals_team_1, goals_team_2, team_1, team_2)
        print(generate_text_for_wins(types[i], roles[0], roles[1]))
    else:
        print(generate_text_for_drafts(types[i]))
