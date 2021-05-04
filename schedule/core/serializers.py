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
        model = Schedule
        fields = ["schedule_date", "schedule_time", "title", "doctor", "doctor_expertise", "doctor_name"]

    doctor_name = serializers.SerializerMethodField('get_doctor_name')
    doctor_expertise = serializers.SerializerMethodField('get_doctor_expertise')

    def get_doctor_name(self, obj):
        return obj.doctor.name

    def get_doctor_expertise(self, obj):
        return obj.doctor.expertise


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "expertise", "schedule_work_time", "available_times"]

    available_times = serializers.SerializerMethodField('get_available_schedule_times')

    def get_available_schedule_times(self, obj):
        times_keys = obj.schedule_work_time.keys()
        times_values = obj.schedule_work_time.values()
        return [times_keys[pos] for pos, i in enumerate(times) if times_values[pos]==True]
