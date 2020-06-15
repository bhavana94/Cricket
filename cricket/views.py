from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,TemplateView
from django.template.response import TemplateResponse

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from cricket.models import Team,Player,PlayerMatchData,MatchData,MatchPoints
from cricket.serializers import CricketTeamSerializer,PlayerListSerializer,MatchesListSerializer,PointListSerializer
from cricket.fixture import fixture_generator

class HomeView(TemplateView):
    template_name = "base.html"

class TeamsView(ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'teams.html'

    def get_queryset(self):
        return Team.objects.all()

class PlayersView(ListView):
    model = Player
    template_name = 'team_detail.html'
    context_object_name = 'teamdetails'

    def get_queryset(self):
        return Player.objects.all()

class TeamDetailsView(ListView):
    model = Player
    template_name = 'team_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeamDetailsView, self).get_context_data(**kwargs)
        players_list = Player.objects.filter(team=self.kwargs['team_id'])
        context['teamdetails'] = players_list
        context['team_team_name']=players_list[0].team
        return context

class PointsTableListingView(ListView):
    model = MatchPoints
    context_object_name = 'points'
    template_name = 'points.html'

    def get_queryset(self):
        return MatchPoints.objects.all()

class FixtureView(ListView):
    model = MatchData
    context_object_name = 'stats'
    template_name = 'matchdata.html'

    def get_queryset(self):
        return MatchData.objects.all()

class Matchschedule(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            fixture_generator()
            return Response({"is_success": True, "message": 'Schedule Generated'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"is_success": False, "message": 'Schedule Not Generated Generated'}, status=status.HTTP_400_BAD_REQUEST)

class CricketTeamList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CricketTeamSerializer

    def list(self, request, *args, **kwargs):
        queryset = CricketTeam.objects.all()
        twc = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": twc.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)

class TeamPlayerList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerListSerializer

    def get(self,request,team_id):
        players = Player.objects.filter(team=team_id)
        serializer = PlayerListSerializer(players, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK,safe=False)


class MatchScheduleList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchesListSerializer

    def list(self, request, *args, **kwargs):
        queryset = MatchData.objects.all()
        match_details = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": match_details.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)


class PointTableList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PointListSerializer

    def list(self, request, *args, **kwargs):
        queryset = MatchPoints.objects.all()
        point_details = self.get_serializer(queryset, many=True)

        data = {"is_status": True, "message": "",
                                    "data": point_details.data,
                     }
        return JsonResponse(data, status=status.HTTP_200_OK)