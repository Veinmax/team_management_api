from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, blank=True, null=True, related_name="members"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
