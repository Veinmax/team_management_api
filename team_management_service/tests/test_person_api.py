from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from team_management_service.models import Person, Team

PERSON_URL = reverse("team_management_service:person-list")


def sample_person(**params):
    defaults = {
        "first_name": "Test Name",
        "last_name": "Test Last",
        "email": "test@gmail.com",
    }
    defaults.update(params)
    return Person.objects.create(**defaults)


class PersonApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_persons(self):
        sample_person()
        response = self.client.get(PERSON_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_person_without_team(self):
        payload = {
            "first_name": "Test Name",
            "last_name": "Test Last",
            "email": "test@gmail.com",
        }
        response = self.client.post(PERSON_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_person_with_team(self):
        Team.objects.create(name="Test Team")
        payload = {
            "first_name": "Test Name",
            "last_name": "Test Last",
            "email": "test@gmail.com",
            "team": 1,
        }
        response = self.client.post(PERSON_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_person(self):
        sample_person()
        response = self.client.get(f"{PERSON_URL}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_person(self):
        sample_person()
        payload = {
            "first_name": "Updated Name",
            "last_name": "Updated Last",
            "email": "updatedtest@gmail.com",
        }
        response = self.client.put(f"{PERSON_URL}1/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_person(self):
        sample_person()
        payload = {
            "first_name": "Updated Name",
        }
        response = self.client.patch(f"{PERSON_URL}1/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        sample_person()
        response = self.client.delete(f"{PERSON_URL}1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
