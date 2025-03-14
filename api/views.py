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

class WorkerEntries(APIView):
    def get(self, request, employee_id):
        try:
            worker = Worker.objects.get(employee_id=employee_id)
            time_entries = TimeEntry.objects.filter(worker=worker)
            if time_entries:
                serializer = TimeEntrySerializer(time_entries, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Worker have no entries'}, status=status.HTTP_404_NOT_FOUND)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)
            

class WorkerLastEntry(APIView):
    def get(self, request, employee_id):
        try:
            worker = Worker.objects.get(employee_id=employee_id)
            last_entry = TimeEntry.objects.filter(worker=worker).order_by('-time').first()
            if last_entry:
                serializer = TimeEntrySerializer(last_entry)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Worker has no entries'}, status=status.HTTP_404_NOT_FOUND)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found'}, status=status.HTTP_404_NOT_FOUND)
