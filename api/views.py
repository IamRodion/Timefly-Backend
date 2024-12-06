from rest_framework import viewsets
from .models import Worker, TimeEntry
from .serializer import WorkerSerializer, TimeEntrySerializer
# Create your views here.

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer