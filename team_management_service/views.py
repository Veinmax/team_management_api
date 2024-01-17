from rest_framework import viewsets
from team_management_service.models import Team, Person
from team_management_service.serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
