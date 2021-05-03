from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Schedule, Doctor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Schedule
        fields = ["schedule_date", "schedule_time", "title", "doctor"]


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Doctor
        fields = ["name", "expertise", "schedule_work_time"]
