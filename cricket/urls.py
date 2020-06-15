from django.conf.urls import url
from cricket.views import *
app_name = "cricket"

urlpatterns = [
	url(r'^$',HomeView.as_view()),
    url(r'^teams/$', TeamsView.as_view(), name='teams'),
    url(r'^players/$', PlayersView.as_view(), name='players'),
    url(r'^team-details/(?P<team_id>[0-9a-f-]+)/$', TeamDetailsView.as_view(), name='team-details'),
    url(r'^points/$', PointsTableListingView.as_view(), name='points'),
    url(r'^fixture/$', FixtureView.as_view(), name='fixture'),
    url(r'^generate-fixture/$', Matchschedule.as_view(), name='generate-fixture'),
    url(r'^rest-api/teams/$', CricketTeamList.as_view(), name='rest-team-lists'),
    url(r'^rest-api/points/$', PointTableList.as_view(), name='rest-points-lists'),
    url(r'^rest-api/player/(?P<team_id>[0-9a-f-]+)/$', TeamPlayerList.as_view(), name='rest-team-player-list'),
    url(r'^rest-api/match/$', MatchScheduleList.as_view(), name='rest-match-list'),
]