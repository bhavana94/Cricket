from itertools import permutations
from cricket.models import Team,MatchData

def fixture_generator():
    """schedule for all the teams present in the Cricket Team table(each team plays twice against one team)"""
    teams = Team.objects.all()
    matches_list = permutations(list(teams),2)
    for i in matches_list:
        MatchData.objects.create(home_team=i[0],away_team=i[1],winner_team=None)
    return True