from django.urls import path, include
from rest_framework import routers
from team_management_service.views import TeamViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register("teams", TeamViewSet)
router.register("persons", PersonViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "team_management_service"
