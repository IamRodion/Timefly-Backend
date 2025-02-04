from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Worker, TimeEntry
from .serializer import WorkerSerializer, TimeEntrySerializer

# Create your views here.
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer

class WorkerByemployeeID(APIView):
    def get(self, request, employee_id):
        try:
            worker = Worker.objects.get(employee_id=employee_id)
            serializer = WorkerSerializer(worker)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)