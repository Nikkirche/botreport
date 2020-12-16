from pprint import pprint


def summery_to_text(summery_data: dict) -> str:
    result = ""
    team_winner = {
        'name_team': summery_data['team_home'],
        'score': int(summery_data['score_home']),
        'possesion': int(summery_data['possesion'].split(":")[0]),
        'attacks': int(summery_data['attacks'].split(':')[0]),
        'yellow_cards': int(summery_data['yellow_cards'].split(':')[0])
    }
    team_loser = {
        'name_team': summery_data['team_away'],
        'score': int(summery_data['score_away']),
        'possesion': int(summery_data['possesion'].split(":")[1]),
        'attacks': int(summery_data['attacks'].split(':')[1]),
        'yellow_cards': int(summery_data['yellow_cards'].split(':')[1])
    }
    pprint(team_winner)

    pprint(team_loser)
    if team_winner['score'] < team_loser['score']:
        team_winner, team_loser = team_loser, team_winner
        result = winner_text(team_winner, team_loser)

    elif team_winner['score'] > team_loser['score']:
        result = winner_text(team_winner, team_loser)
    else:
        result = draw_text(team_winner, team_loser)
    print(result)
    return result


def winner_text(team_winner: dict, team_loser: dict) -> str:
    result = []
    result.append(f"And the match between {team_winner['name_team']} and {team_loser['name_team']} " \
                      f"ends with the score of {team_winner['score']}:{team_loser['score']}.")

    if team_winner['possesion'] <= team_loser['possesion']:
        result.append(f"Despite having less possession of the ball, {team_winner['name_team']}" \
                          f" wins! {team_winner['possesion']}%.")
    else:
        result.append(f"{team_winner['name_team']} possessed the ball for the entire game! No surprise they've won." \
                          f" {team_winner['possesion']}%.")

    result.append(
        f'{team_winner["name_team"]} and {team_loser["name_team"]} have received {team_winner["yellow_cards"]} '
        f'and {team_loser["yellow_cards"]} yellow cards respectively.')

    if team_winner['attacks'] >= team_loser['attacks']:
        result.append(f"A series of carefully planned attacks from {team_winner['attacks']} "
                      f"has led them to a win – {team_winner['attacks']}:{team_loser['attacks']}.")
    else:
        result.append(f"Unsuccessful attacks from {team_loser['name_team']} "
                      f"haven’t saved them from a defeat – {team_loser['attacks']}:{team_winner['attacks']}.")
    if team_loser['attacks'] + team_winner['attacks'] > 170:
        result.append("Extremely intense play – lots of attacks from both sides!")
    else:
        result.append("The match hasn’t got really intense – not many interesting attacks from any side.")
    if team_winner['score'] - team_loser['score'] >= 2:
        result.append(f'A professional play throughout the match – {team_winner["name_team"]} '
                      f'have shown their superiority.')
    else:
        result.append(f'Even after the end of the match, the victory of {team_winner["name_team"]} isn’t obvious.')
    return " ".join(el for el in result)


def draw_text(team_winner: dict, team_loser: dict) -> str:
    return "DRAW!!!"