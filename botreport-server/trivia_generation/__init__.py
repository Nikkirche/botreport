import infodata
from random import random, choice
from infodata import InfoSource, sportsdb


class InfoAggregator:
    def __init__(self, sources: list):
        self.sources = sources

    def add(self, source: InfoSource):
        self.sources.append(source)

    def get_team(self, query: str):
        team = infodata.Team
        for source in self.sources:
            data = source.get_team(query)
            infodata.merge_from(data, team)
        return team

    def get_player(self, query: str):
        player = infodata.Player
        for source in self.sources:
            data = source.get_player(query)
            infodata.merge_from(data, player)
        return player


class TriviaGenerator:
    def __init__(self, aggregator: InfoAggregator, templates_team: dict, templates_player: dict):
        self.aggregator = aggregator
        self.templates_team = templates_team
        self.templates_player = templates_player

    def __trivia(self, data, templates):
        data = {key: value for key, value in data.items() if value}
        textlets = []
        # TODO: generate trivia text from data
        for template in templates.keys():
            # Data to templates
            if template == 'sep':
                # Separators are processed later
                continue
            found = True
            for attribute in template:
                if attribute not in data.keys():
                    found = False
                    break
            if not found:
                # Skipping the template: required attributes not set
                continue

            t = choice(templates[template])
            textlets.append(t)

        # Glueing together
        text = ' '.join(textlets)

        for i in range(text.count('$sep')):
            text = text.replace('$sep', choice(
                templates['sep']), 1)

        # Filling in the templates
        text = text.format(**data)
        return text

    def trivia_player(self, query: str):
        player = self.aggregator.get_player(query)
        return self.__trivia(player, self.templates_player)

    def trivia_team(self, query: str):
        team = self.aggregator.get_team(query)
        return self.__trivia(team, self.templates_team)

    def trivia_event(self, event: dict):
        priority_player = False
        text = ''

        if event['event'] in ('YELLOW_CARD', 'YELLOW_RED_CARD', 'RED_CARD'):
            priority_player = True
        if priority_player or random() <= 0.4:
            variants = [
                event['player'],
                ' '.join(event['player'].split()[::-1]),
                event['player'].split()[0],
            ]
            for var in variants:
                try:
                    text = self.trivia_player(var)
                except Exception as e:
                    # Player not found. Trying another variation...
                    continue
        if not text:
            if event['home_away'] == 'h':
                team_name = event['team_home']
            else:
                team_name = event['team_away']
            try:
                text = self.trivia_team(team_name)
            except Exception as e:
                pass
        return text
            

default_player = {
    ('name',): ('{name} is a footballer', '{name} is', 'The unmatched {name} is', 'An excellent player, {name} is', 'Truly a legend! {name} is',),
    ('country_born',): ('from {country_born}', 'coming from {country_born}',),
    ('country_play', 'team'): ('$sep plays for {country_play}, team {team}', '$sep plays for {team}',),
    ('date_born',): ('$sep was born on {date_born}',),
    ('height',): ('$sep is {height} tall', '$sep is of {height}',),
    ('weight',): ('$sep weighs {weight}', '$sep has {weight} of weight',),

    'sep': (',', ' and', '. {name}', ';')
}

default_team = {
    ('name',): ('{name} is a team', 'Team {name} is', 'The undefeatable {name} is',),
    ('country',): ('from {country}', 'coming from {country}',),
    ('year_founded',): ('$sep was founded in {year_founded}', '. Founded in {year_founded}, {name} is standing strong today', ''),
    ('league_1',): ('$sep participates in {league_1}', '$sep plays in leagues, like {league_1}',),
    ('league_2',): ('$sep also plays in {league_2}', '$sep is also a member of {league_2}',),
    ('league_3',): ('$sep plays in {league_3} from time to time', '. Occasionally {name} plays for {league_3}',),
    ('league_4',): ('$sep takes part in many others',),

    'sep': (',', ' and', '. {name}', '. It', '. The team', ';')
}

if __name__ == "__main__":
    sapi = sportsdb.SportsDBInfoSource()

    aggregator = InfoAggregator([sapi])
    generator = TriviaGenerator(aggregator, default_team, default_player)


    event = {
        'id': '21674053',
        'match_id': '225702',
        'player': 'BARELLA NICOLO',
        'time': '84',
        'event': 'GOAL',
        'sort': '5',
        'home_away': 'a', 
        'score_home': 1, 
        'score_away': 2, 
        'team_home': 'Cagliari', 
        'team_away': 'Inter', 
    }
    
    real_trivia = generator.trivia_event(event)
    print(real_trivia)