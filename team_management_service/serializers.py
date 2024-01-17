from rest_framework import serializers
from team_management_service.models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    team_members = serializers.PrimaryKeyRelatedField(
        source="members", many=True, read_only=True
    )

    class Meta:
        model = Team
        fields = ("id", "name", "team_members")


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "first_name", "last_name", "email", "team")
