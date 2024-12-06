from rest_framework import serializers
from .models import Worker, TimeEntry

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields='__all__'


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=TimeEntry
        fields='__all__'