from django.contrib import admin
from .models import Delivery, Match, Umpire


class DelivertAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'batting_team', 'bowling_team', 'over',
                    'ball', 'batsman', 'non_striker', 'bowler', 'batsman_runs',
                    'total_runs')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'team1', 'team2', 'toss_winner',
                    'toss_decision', 'winner', 'umpire1', 'umpire2')


class UmpireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality')


admin.site.register(Umpire, UmpireAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Delivery, DelivertAdmin)
