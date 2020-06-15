from rest_framework import serializers
from cricket.models import Team,Player,PlayerMatchData,MatchData,MatchPoints

class CricketTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'team_name', 'logo')


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name','picture')



class MatchesListSerializer(serializers.ModelSerializer):
    home_team= serializers.SerializerMethodField()
    away_team= serializers.SerializerMethodField()
    winner_team= serializers.SerializerMethodField()

    def get_home_team(self,obj):
        return obj.home_team.team_name

    def get_away_team(self,obj):
        return obj.away_team.team_name

    def get_winner_team(self,obj):
        if obj.winner_team is not None:
            return obj.winner_team.team_name
        else:
            return 'Match Yet To be played'

    class Meta:
        model = MatchData
        fields = ('home_team','away_team','winner_team')


class PointListSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()

    def get_team(self,obj):
        return obj.team.team_name

    class Meta:
        model = MatchPoints
        fields = '__all__'