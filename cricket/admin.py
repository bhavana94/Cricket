from django.contrib import admin
from .models import Team,Player,PlayerMatchData,MatchData,MatchPoints
# Register your models here.
from django.core.exceptions import ValidationError



class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'logo', 'club_state', 'date_created', 'date_updated')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team','picture', 'jersey_number', 'origin_country', 'date_created',
                    'date_updated')

class MatchDataAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'winner_team', 'date_created', 'date_created')

class MatchPointsAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

class PlayerMatchDataAdmin(admin.ModelAdmin):
    list_display = ('player', 'no_of_matches', 'total_runs', 'total_wickets', 'total_centuries', 'total_fifties',
                    'highest_score', 'date_created','date_updated')


admin.site.register(Team,TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(MatchData, MatchDataAdmin)
admin.site.register(MatchPoints, MatchPointsAdmin)
admin.site.register(PlayerMatchData, PlayerMatchDataAdmin)