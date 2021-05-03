from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet, DoctorViewSet, ScheduleViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"doctors", DoctorViewSet)
router.register(r"schedules", ScheduleViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
]
