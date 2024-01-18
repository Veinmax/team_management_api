from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from team_management_service.models import Team

TEAM_URL = reverse("team_management_service:team-list")


class TeamApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_teams(self):
        Team.objects.create(name="Test Team")
        response = self.client.get(TEAM_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_team(self):
        payload = {"name": "Test Team"}
        response = self.client.post(TEAM_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_team(self):
        Team.objects.create(name="Test Team")
        response = self.client.get(f"{TEAM_URL}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_team(self):
        Team.objects.create(name="Test Team")
        payload = {"name": "Updated Test Team"}
        response = self.client.put(f"{TEAM_URL}1/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_team(self):
        Team.objects.create(name="Test Team")
        response = self.client.delete(f"{TEAM_URL}1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
